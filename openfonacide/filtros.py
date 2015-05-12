import json
from django.db import connection
from openfonacide.views import JSONResponse


def filtros(request):
    nombre = request.GET.get('f')
    if nombre == 'fonacide':
        # print type(filtro_fonacide())
        # print filtro_fonacide()
        return JSONResponse(json.loads(filtro_fonacide()))
    elif nombre == 'prioridad':
        tipo = request.GET.getlist('tipo')
        rango = request.GET.getlist('rango')
        rango = get_rango(rango)
        if tipo:
            return JSONResponse(json.loads(filtro_prioridad(tipo, rango)))
    return JSONResponse([])

def get_rango(rango):
    if len(rango) != 2:
        return [0, 200]
    try:
        rango0 = int(rango[0])
        rango1 = int(rango[1])
        if rango0 > rango1:
            rango0, rango1 = rango1, rango0
        if rango0 == rango1:
            rango0 = 0
            rango1 = 200
        if rango0 >= 200 or rango1 > 200:
            rango0 = 0
            rango1 = 200
    except ValueError:
        rango0 = 0
        rango1 = 200
    ret = [rango0, rango1]
    return ret


def filtro_prioridad(tipo, rango):
    print tipo
    cursor = connection.cursor()
    cursor.execute(query_prioridad(tipo, rango))
    rows = cursor.fetchall()
    rows = map(lambda x: x[0], rows)
    return json.dumps(rows)


def query_prioridad(tipo, rango):
    begin_query = ('SELECT DISTINCT codigo_establecimiento FROM (')
    union = False
    if tipo == 'mobiliarios' or 'mobiliarios' in tipo:
        begin_query += ('SELECT DISTINCT es.codigo_establecimiento, '
                'p_mob.periodo FROM openfonacide_establecimiento es '
                'JOIN openfonacide_institucion inst '
                'ON es.codigo_establecimiento = inst.codigo_establecimiento '
                'LEFT JOIN openfonacide_mobiliario p_mob '
                'ON p_mob.codigo_institucion = inst.codigo_institucion '
                'OR p_mob.codigo_establecimiento = es.codigo_establecimiento '
                'where p_mob.numero_prioridad >= '+ str(rango[0]) +
                ' and p_mob.numero_prioridad <= ' + str(rango[1]))
        union = True
    if tipo == 'sanitarios' or 'sanitarios' in tipo:
        if union:
            begin_query += 'UNION '
        begin_query += ('SELECT DISTINCT es.codigo_establecimiento, '
                'p_san.periodo FROM openfonacide_establecimiento es '
                'JOIN openfonacide_institucion inst '
                'ON es.codigo_establecimiento = inst.codigo_establecimiento '
                'LEFT JOIN openfonacide_sanitario p_san '
                'ON p_san.codigo_institucion = inst.codigo_institucion '
                'OR p_san.codigo_establecimiento = es.codigo_establecimiento '
                'where p_san.numero_prioridad >= '+ str(rango[0]) +
                ' and p_san.numero_prioridad <= ' + str(rango[1]))
        union = True
    if tipo == 'aulas' or 'aulas' in tipo:
        if union:
            begin_query += 'UNION '
        begin_query += ('SELECT DISTINCT es.codigo_establecimiento, '
                'p_au.periodo FROM openfonacide_establecimiento es '
                'JOIN openfonacide_institucion inst '
                'ON es.codigo_establecimiento = inst.codigo_establecimiento '
                'LEFT JOIN openfonacide_espacio p_au '
                'ON p_au.codigo_institucion = inst.codigo_institucion '
                'OR p_au.codigo_establecimiento = es.codigo_establecimiento '
                ' where p_au.nombre_espacio like \'%AULA%\' '
                ' and p_au.numero_prioridad >= ' + str(rango[0]) +
                ' and p_au.numero_prioridad <= ' + str(rango[1]))
        union = True
    if tipo == 'otros' or 'otros' in tipo:
        if union:
            begin_query += 'UNION '
        begin_query += ('SELECT DISTINCT es.codigo_establecimiento, '
                'p_es.periodo FROM openfonacide_establecimiento es '
                'JOIN openfonacide_institucion inst '
                'ON es.codigo_establecimiento = inst.codigo_establecimiento '
                'LEFT JOIN openfonacide_espacio p_es '
                'ON p_es.codigo_institucion = inst.codigo_institucion '
                'OR p_es.codigo_establecimiento = es.codigo_establecimiento '
                ' where p_es.nombre_espacio not like \'%AULA%\' '
                ' and p_es.numero_prioridad >= ' + str(rango[0]) +
                ' and p_es.numero_prioridad <= ' + str(rango[1]))
    begin_query += ") other where other.periodo is not null"
    if not union:
        return "SELECT 1 WHERE 1 = 0"
    return begin_query

def filtro_fonacide():
    cursor = connection.cursor()
    cursor.execute('SELECT DISTINCT codigo_establecimiento FROM '
                    '(SELECT DISTINCT es.codigo_establecimiento, '
                    'p_es.periodo FROM openfonacide_establecimiento es '
                    'JOIN openfonacide_institucion inst '
                    'ON es.codigo_establecimiento = inst.codigo_establecimiento '
                    'LEFT JOIN openfonacide_espacio p_es '
                    'ON p_es.codigo_institucion = inst.codigo_institucion '
                    'OR p_es.codigo_establecimiento = es.codigo_establecimiento '
                    'UNION '
                    'SELECT DISTINCT es.codigo_establecimiento, p_mob.periodo '
                    'FROM openfonacide_establecimiento es '
                    'JOIN openfonacide_institucion inst '
                    'ON es.codigo_establecimiento = inst.codigo_establecimiento '
                    'LEFT JOIN openfonacide_mobiliario p_mob '
                    'ON p_mob.codigo_institucion = inst.codigo_institucion '
                    'OR p_mob.codigo_establecimiento = es.codigo_establecimiento '
                    'UNION '
                    'SELECT DISTINCT es.codigo_establecimiento, p_san.periodo '
                    'FROM openfonacide_establecimiento es '
                    'JOIN openfonacide_institucion inst '
                    'ON es.codigo_establecimiento = inst.codigo_establecimiento '
                    'JOIN openfonacide_sanitario p_san '
                    'ON p_san.codigo_institucion = inst.codigo_institucion '
                    'OR p_san.codigo_establecimiento = es.codigo_establecimiento) other '
                    'where other.periodo is not null')
    rows = cursor.fetchall()
    rows = map(lambda x: x[0], rows)
    return json.dumps(rows)
