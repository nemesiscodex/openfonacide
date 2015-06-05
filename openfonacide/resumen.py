import json
from django.db import connection
from multiprocessing import Process, Queue
from django.http import JsonResponse


def _resumen(request):
    params = request.GET.get('params')
    if params:
        params = json.loads(params)
        return JsonResponse(generar_query(params), safe=False)
    return JsonResponse([], safe=False)


def generar_query(params):
    periodo = params.get('anios')
    ubicaciones = params.get('ubicaciones')
    prioridades = params.get('prioridades')
    estados = params.get('estado')
    dncp = params.get('dncp')

    if periodo is None:
        periodo = '2015'

    if estados is None:
        estados = {'estado': None, 'informes': False}
    else:
        if not estados.get('estado') or estados.get('estado') not in ('priorizado', 'planificado', 'adjudicado', 'terminado'):
            estados['estado'] = None

    if dncp is None:
        dncp = {'adjudicaciones': False, 'planificaciones': False}

    if prioridades is None:
        prioridades = {'aulas': True, 'mobiliarios': True, 'sanitarios': True, 'otros': True}

    dict_prioridades = {}
    ret_elegibles = Queue()
    ret_beneficiarios_pedidos = Queue()
    ret_top_establecimientos = Queue()
    ret_tipo_requerimiento = Queue()
    p1 = Process(target=elegibles, args=(periodo, prioridades, ubicaciones, estados, dncp, ret_elegibles))
    p1.start()
    p2 = Process(target=beneficiarios_pedidos, args=(periodo, prioridades, ubicaciones, estados, dncp, ret_beneficiarios_pedidos))
    p2.start()
    # p3 = Process(target=top_establecimientos, args=(periodo, prioridades, ubicaciones, ret_top_establecimientos))
    # p3.start()
    p4 = Process(target=tipo_requerimiento, args=(periodo, prioridades, ubicaciones, estados, dncp, ret_tipo_requerimiento))
    p4.start()
    p1.join()
    p2.join()
    # p3.join()
    p4.join()
    dict_prioridades['estados'] = estados
    dict_prioridades['ubicaciones'] = ubicaciones
    dict_prioridades['prioridades'] = prioridades
    dict_prioridades['periodo'] = periodo
    dict_prioridades['dncp'] = dncp
    dict_prioridades['elegibles'] = ret_elegibles.get()
    dict_prioridades['beneficiarios'] = ret_beneficiarios_pedidos.get()
    # dict_prioridades['top_establecimientos'] = ret_top_establecimientos.get()
    dict_prioridades['tipo_requerimiento'] = ret_tipo_requerimiento.get()
    return dict_prioridades


def elegibles(periodo, prioridades, ubicaciones, estados, dncp, ret):
    query = 'SELECT count(DISTINCT codigo_institucion) FROM ('
    cursor = connection.cursor()
    estado = estados.get('estado')
    documentos = estados.get('informes')

    query_join_institucion = ' JOIN openfonacide_institucion inst ON inst.codigo_institucion = %s.codigo_institucion '

    query_dncp = ''
    if dncp.get('adjudicaciones'):
        query_dncp += ' JOIN openfonacide_institucion_adjudicaciones adju ON adju.institucion_id = inst.id '
    if dncp.get('planificaciones'):
        query_dncp += ' JOIN openfonacide_institucion_planificaciones planif ON planif.institucion_id = inst.id '

    if len(query_dncp) > 0:
        query_dncp = query_join_institucion + query_dncp

    query_estado = ''
    if estado and estado.lower() in ('priorizado', 'planificado', 'adjudicado', 'terminado'):
        query_estado = " AND lower(estado_de_obra) = '%s' " % estado

    query_documentos = ''
    if documentos:
        query_documentos = ' AND documento IS NOT NULL '

    union = False
    if prioridades.get('mobiliarios'):
        query += ('SELECT DISTINCT m.codigo_institucion '
                  'FROM openfonacide_mobiliario m '
                  'JOIN openfonacide_establecimiento es on m.codigo_establecimiento = es.codigo_establecimiento ')
        if len(query_dncp) > 0:
            query += query_dncp % 'm'
        query += ('WHERE m.periodo = \''+periodo + '\' ')
        query += query_estado
        query += query_documentos
        query += generar_query_ubicaciones(ubicaciones, 'es')
        union = True
    if prioridades.get('aulas'):
        if union:
            query+= ' UNION '
        query += ('SELECT DISTINCT au.codigo_institucion '
                  'FROM openfonacide_espacio au '
                  'JOIN openfonacide_establecimiento es on au.codigo_establecimiento = es.codigo_establecimiento ')
        if len(query_dncp) > 0:
            query += query_dncp % 'au'
        query += ('WHERE au.periodo = \''+periodo + '\' '
                  'AND au.nombre_espacio IS NULL ')
        query += query_estado
        query += query_documentos
        query += generar_query_ubicaciones(ubicaciones, 'es')
        union = True
    if prioridades.get('otros'):
        if union:
            query+= ' UNION '
        query += ('SELECT DISTINCT o.codigo_institucion '
                  'FROM openfonacide_espacio o '
                  'JOIN openfonacide_establecimiento es on o.codigo_establecimiento = es.codigo_establecimiento ')
        if len(query_dncp) > 0:
            query += query_dncp % 'o'
        query += ('WHERE o.periodo = \''+periodo + '\' '
                  'AND o.nombre_espacio IS NOT NULL ')
        query += query_estado
        query += query_documentos
        query += generar_query_ubicaciones(ubicaciones, 'es')
        union = True
    if prioridades.get('sanitarios'):
        if union:
            query+= ' UNION '
        query += ('SELECT DISTINCT sa.codigo_institucion '
                  'FROM openfonacide_sanitario sa '
                  'JOIN openfonacide_establecimiento es on sa.codigo_establecimiento = es.codigo_establecimiento ')
        if len(query_dncp) > 0:
            query += query_dncp % 'sa'
        query += ('WHERE sa.periodo = \''+periodo + '\' ')
        query += query_estado
        query += query_documentos
        query += generar_query_ubicaciones(ubicaciones, 'es')
        union = True
    query += ') otros'

    if not union:
        ret.put(0)
        return
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    ret.put(result[0])
    return


def beneficiarios_pedidos(periodo, prioridades, ubicaciones, estados, dncp, ret):
    union = False
    cursor = connection.cursor()

    estado = estados.get('estado')
    documentos = estados.get('informes')

    query_estado = ''
    if estado and estado.lower() in ('priorizado', 'planificado', 'adjudicado', 'terminado'):
        query_estado = " AND lower(estado_de_obra) = '%s' " % estado

    query_documentos = ''
    if documentos:
        query_documentos = ' AND documento IS NOT NULL '

    query_join_institucion = ' JOIN openfonacide_institucion inst ON inst.codigo_institucion = %s.codigo_institucion '

    query_dncp = ''
    if dncp.get('adjudicaciones'):
        query_dncp += ' JOIN openfonacide_institucion_adjudicaciones adju ON adju.institucion_id = inst.id '
    if dncp.get('planificaciones'):
        query_dncp += ' JOIN openfonacide_institucion_planificaciones planif ON planif.institucion_id = inst.id '

    if len(query_dncp) > 0:
        query_dncp = query_join_institucion + query_dncp

    query = ''
    if prioridades.get('mobiliarios'):
        query += ('SELECT \'Mobiliarios\'  AS tipo, '
                  'count(*)      AS cantidad, '
                  'sum(CAST(cantidad_requerida AS INT)) AS cantidad_requerida, '
                  'sum(CAST(numero_beneficiados AS INT)) AS beneficiados, '
                  'round(sum(CAST(numero_beneficiados AS INT)) / sum(CAST(cantidad_requerida AS FLOAT))) AS promedio '
                  'FROM openfonacide_mobiliario m '
                  'JOIN openfonacide_establecimiento es on m.codigo_establecimiento = es.codigo_establecimiento ')
        if len(query_dncp) > 0:
            query += query_dncp % 'm'
        query += ('WHERE cantidad_requerida ~ E\'^\\\\d+$\' AND numero_beneficiados ~ E\'^\\\\d+$\' AND m.periodo = \''+periodo+'\' ')
        query += query_estado
        query += query_documentos
        query += generar_query_ubicaciones(ubicaciones, 'es')
        union = True
    if prioridades.get('aulas'):
        if union:
            query+= ' UNION '
        query += ('SELECT \'Aulas\'	     AS tipo, '
                  'count(*)	    AS cantidad, '
                  'sum(CAST(cantidad_requerida AS  INT))	AS cantidad_requerida, '
                  'sum(CAST(numero_beneficiados AS INT))	AS beneficiados, '
                  'round(sum(CAST(numero_beneficiados AS INT)) / sum(CAST(cantidad_requerida AS FLOAT))) AS promedio '
                  'FROM openfonacide_espacio au '
                  'JOIN openfonacide_establecimiento es on au.codigo_establecimiento = es.codigo_establecimiento ')
        if len(query_dncp) > 0:
            query += query_dncp % 'au'
        query += ('WHERE '
                  'cantidad_requerida ~ E\'^\\\\d+$\' AND numero_beneficiados ~ E\'^\\\\d+$\' '
                  'AND au.periodo = \''+periodo+'\' AND nombre_espacio IS NULL ')
        query += query_estado
        query += query_documentos
        query += generar_query_ubicaciones(ubicaciones, 'es')
        union = True
    if prioridades.get('otros'):
        if union:
            query+= ' UNION '
        query += ('SELECT \'Otros espacios\' AS tipo, '
                  'count(*)  AS cantidad, '
                  'sum(CAST(cantidad_requerida AS INT))  AS cantidad_requerida, '
                  'sum(CAST(numero_beneficiados AS INT)) AS beneficiados, '
                  'round(sum(CAST(numero_beneficiados AS INT)) / sum(CAST(cantidad_requerida AS FLOAT))) AS promedio '
                  'FROM openfonacide_espacio o '
                  'JOIN openfonacide_establecimiento es on o.codigo_establecimiento = es.codigo_establecimiento ')
        if len(query_dncp) > 0:
            query += query_dncp % 'o'
        query += ('WHERE '
                  'cantidad_requerida ~ E\'^\\\\d+$\' AND numero_beneficiados ~ E\'^\\\\d+$\' '
                  'AND o.periodo = \''+periodo+'\' AND nombre_espacio IS NOT NULL ')
        query += query_estado
        query += query_documentos
        query += generar_query_ubicaciones(ubicaciones, 'es')
        union = True
    if prioridades.get('sanitarios'):
        if union:
            query+= ' UNION '
        query += ('SELECT \'Sanitarios\'	AS tipo, '
                  'count(*)	    AS cantidad, '
                  'sum(CAST(cantidad_requerida AS INT))	AS cantidad_requerida, '
                  'sum(CAST(numero_beneficiados AS INT))	AS beneficiados, '
                  'round(sum(CAST(numero_beneficiados AS INT)) / sum(CAST(cantidad_requerida AS FLOAT))) AS promedio '
                  'FROM openfonacide_sanitario sa '
                  'JOIN openfonacide_establecimiento es on sa.codigo_establecimiento = es.codigo_establecimiento ')
        if len(query_dncp) > 0:
            query += query_dncp % 'sa'
        query += ('WHERE cantidad_requerida ~ E\'^\\\\d+$\' AND numero_beneficiados ~ E\'^\\\\d+$\' AND sa.periodo = \''+periodo+'\' ')
        query += query_estado
        query += query_documentos
        query += generar_query_ubicaciones(ubicaciones, 'es')
        union = True
    if query == '':
        ret.put([])
        return
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    ret.put(results)


def top_establecimientos(periodo, prioridades, ubicaciones, ret):
    query = ('SELECT COUNT(DISTINCT codigo_institucion) AS instituciones_elegibles, '
            'codigo_establecimiento FROM ( ')
    cursor = connection.cursor()
    union = False
    if prioridades.get('mobiliarios'):
        query += ('SELECT '
                  'm.codigo_institucion, '
                  'm.codigo_establecimiento '
                  'FROM openfonacide_mobiliario m '
                  'JOIN openfonacide_establecimiento es on m.codigo_establecimiento = es.codigo_establecimiento '
                  'WHERE periodo = \'' + periodo + '\' ')
        query += generar_query_ubicaciones(ubicaciones, 'es')
        union = True
    if prioridades.get('aulas'):
        if union:
            query+= ' UNION  '
        query += ('SELECT '
                  'au.codigo_institucion, '
                  'au.codigo_establecimiento '
                  'FROM openfonacide_espacio au '
                  'JOIN openfonacide_establecimiento es on au.codigo_establecimiento = es.codigo_establecimiento '
                  'WHERE periodo = \'' + periodo + '\' '
                  'AND nombre_espacio IS NULL')
        query += generar_query_ubicaciones(ubicaciones, 'es')
        union = True
    if prioridades.get('otros'):
        if union:
            query+= ' UNION '
        query += ('SELECT '
                  'o.codigo_institucion, '
                  'o.codigo_establecimiento '
                  'FROM openfonacide_espacio o '
                  'JOIN openfonacide_establecimiento es on o.codigo_establecimiento = es.codigo_establecimiento '
                  'WHERE periodo = \'' + periodo + '\' '
                  'AND nombre_espacio IS NOT NULL')
        query += generar_query_ubicaciones(ubicaciones, 'es')
        union = True
    if prioridades.get('sanitarios'):
        if union:
            query+= ' UNION '
        query += ('SELECT '
                  'sa.codigo_institucion, '
                  'sa.codigo_establecimiento '
                  'FROM openfonacide_sanitario sa '
                  'JOIN openfonacide_establecimiento es on sa.codigo_establecimiento = es.codigo_establecimiento '
                  'WHERE periodo = \'' + periodo + '\' ')
        query += generar_query_ubicaciones(ubicaciones, 'es')
        union = True

    query += (') otros '
              'GROUP BY codigo_establecimiento '
              'HAVING COUNT(DISTINCT codigo_institucion) > 2 '
              'ORDER BY instituciones_elegibles DESC '
              'LIMIT 10 ')
    if not union:
        ret.put([])
        return
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    ret.put(results)


def tipo_requerimiento(periodo, prioridades, ubicaciones, estados, dncp, ret):
    query = ''
    cursor = connection.cursor()
    union = False
    estado = estados.get('estado')
    documentos = estados.get('informes')

    query_estado = ''
    if estado and estado.lower() in ('priorizado', 'planificado', 'adjudicado', 'terminado'):
        query_estado = " AND lower(estado_de_obra) = '%s' " % estado

    query_documentos = ''
    if documentos:
        query_documentos = ' AND documento IS NOT NULL '

    query_join_institucion = ' JOIN openfonacide_institucion inst ON inst.codigo_institucion = %s.codigo_institucion '

    query_dncp = ''
    if dncp.get('adjudicaciones'):
        query_dncp += ' JOIN openfonacide_institucion_adjudicaciones adju ON adju.institucion_id = inst.id '
    if dncp.get('planificaciones'):
        query_dncp += ' JOIN openfonacide_institucion_planificaciones planif ON planif.institucion_id = inst.id '

    if len(query_dncp) > 0:
        query_dncp = query_join_institucion + query_dncp

    if prioridades.get('otros'):
        query += ('SELECT \'otros\'                              AS tipo, '
                  'count(*)                             AS pedidos, '
                  'sum(CAST(cantidad_requerida AS INT)) AS requerida, '
                  'tipo_requerimiento_infraestructura '
                  'FROM openfonacide_espacio o '
                  'JOIN openfonacide_establecimiento es on o.codigo_establecimiento = es.codigo_establecimiento ')
        if len(query_dncp) > 0:
            query += query_dncp % 'o'
        query += ('WHERE nombre_espacio IS NOT NULL AND cantidad_requerida ~ E\'^\\\\d+$\' '
                  'AND o.periodo = \'' + periodo + '\' ')
        query += query_estado
        query += query_documentos
        query += generar_query_ubicaciones(ubicaciones, 'es')
        query += ' GROUP BY tipo_requerimiento_infraestructura '
        union = True
    if prioridades.get('aulas'):
        if union:
            query+= ' UNION '
        query += ('SELECT \'aulas\'                              AS tipo, '
                  'count(*)                             AS pedidos, '
                  'sum(CAST(cantidad_requerida AS INT)) AS requerida, '
                  'tipo_requerimiento_infraestructura '
                  'FROM openfonacide_espacio au '
                  'JOIN openfonacide_establecimiento es on au.codigo_establecimiento = es.codigo_establecimiento ')
        if len(query_dncp) > 0:
            query += query_dncp % 'au'
        query += ('WHERE nombre_espacio IS NULL AND cantidad_requerida ~ E\'^\\\\d+$\' '
                  'AND au.periodo = \'' + periodo + '\' ')
        query += query_estado
        query += query_documentos
        query += generar_query_ubicaciones(ubicaciones, 'es')
        query += 'GROUP BY tipo_requerimiento_infraestructura '
        union = True
    if prioridades.get('sanitarios'):
        if union:
            query+= ' UNION '
        query += ('SELECT \'sanitario\'                          AS tipo, '
                  'count(*)                             AS pedidos, '
                  'sum(CAST(cantidad_requerida AS INT)) AS requerida, '
                  'tipo_requerimiento_infraestructura '
                  'FROM openfonacide_sanitario sa '
                  'JOIN openfonacide_establecimiento es on sa.codigo_establecimiento = es.codigo_establecimiento ')
        if len(query_dncp) > 0:
            query += query_dncp % 'sa'
        query += ('WHERE cantidad_requerida ~ E\'^\\\\d+$\' '
                  'AND sa.periodo = \'' + periodo + '\' ')
        query += query_estado
        query += query_documentos
        query += generar_query_ubicaciones(ubicaciones, 'es')
        query += 'GROUP BY tipo_requerimiento_infraestructura '
    if query == '':
        ret.put([])
        return
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    ret.put(results)


def generar_query_ubicaciones(ubicaciones, tabla_prioridad):
    query = ''
    count = 0
    if type(ubicaciones) != list:
        return query
    for ubicacion in ubicaciones:
        query_ubicacion = ''
        if len(ubicacion) != 3:
            continue
        dep_id = ubicacion[0]
        if dep_id:
            query_ubicacion += ' ' + tabla_prioridad + '.codigo_departamento = \'' + dep_id + '\' '

        dis_id = ubicacion[1]
        if dis_id:
            query_ubicacion += ' AND '
            query_ubicacion += ' ' + tabla_prioridad + '.codigo_distrito = \'' + dis_id + '\' '

        bar_id = ubicacion[2]
        if bar_id:
            query_ubicacion += ' AND '
            query_ubicacion += ' ' + tabla_prioridad + '.codigo_barrio_localidad = \'' + bar_id + '\' '

        if count == 0:
            query += '('
        else:
            query += ' OR '
        query += '(' + query_ubicacion + ')'

        count += 1
    if query != '':
        query += ')'
        query = ' AND ' + query

    return query


