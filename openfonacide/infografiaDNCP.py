import json
from django.db import connection
from multiprocessing import Process, Queue
from django.http import JsonResponse



def infografiaDNCP(request):
    filtro = request.GET.get('filtro')
    opcion = request.GET.get('opcion')  
    anio = request.GET.get('anio') 

    if opcion =="Municipalidades":
        opcion= 'LIKE \'%Muni%\' '
    elif opcion == "Gobernaciones":
        opcion= 'LIKE \'%Gobierno Departamental%\' '
    else:
        opcion= 'NOT LIKE \'%Muni%\' AND  p.convocante NOT LIKE \'%Gobierno Departamental%\' '     
    if filtro and opcion :        
        return JsonResponse(generar_query(filtro,opcion,anio), safe=False)
    return JsonResponse([], safe=False)


def generar_query(filtro,opcion,anio):

    query = Queue()
    dict_respuesta = {}  
   
    if filtro == "cantidad_adjudicaciones":
      print "cantidad_adjudicaciones"
      p1 = Process(target=cantidad_adjudicaciones, args=(filtro, opcion,anio, query))
      p1.start()        
      p1.join()
      dict_respuesta['cantidad_adjudicaciones'] = query.get()
    elif filtro == "monto_adjudicaciones":
      print 'monto_adjudicaciones'
      p1 = Process(target=monto_adjudicaciones, args=(filtro, opcion,anio, query))
      p1.start()        
      p1.join()
      dict_respuesta['monto_adjudicaciones'] = query.get()
    elif filtro == "categoria":
      print 'categoria'
      p1 = Process(target=categoria, args=(filtro, opcion,anio, query))
      p1.start()        
      p1.join()
      dict_respuesta['categoria'] = query.get()
    elif filtro == "procedimiento":
      print 'procedimiento'
      p1 = Process(target=procedimiento, args=(filtro, opcion,anio, query))
      p1.start()        
      p1.join()
      dict_respuesta['procedimiento'] = query.get()  


    return dict_respuesta


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def cantidad_adjudicaciones(filtro, opcion, anio, ret):
    query = ('SELECT  p.convocante, COUNT(*) cantidad '
            'FROM openfonacide_adjudicacion a, openfonacide_planificacion p ' 
            'WHERE a.id_llamado=p.id_llamado '
            'AND p.etiquetas=\'fonacide\' AND  p.convocante  '+opcion + 
            'AND anio=\''+ anio + '\' '
            'GROUP BY  p.convocante ORDER BY cantidad DESC')

    cursor = connection.cursor()
    print query

    
  
    cursor.execute(query)
    result = dictfetchall(cursor)
    cursor.close()
    ret.put(result)
    return


def monto_adjudicaciones(filtro, opcion,  anio, ret):
    query = ('SELECT  p.convocante, SUM(a.monto_total_adjudicado::float) monto_total '
            'FROM openfonacide_adjudicacion a, openfonacide_planificacion p ' 
            'WHERE a.id_llamado=p.id_llamado '
            'AND p.etiquetas=\'fonacide\' AND  p.convocante  ' + opcion + 
            'AND anio=\''+ anio + '\' '
            'GROUP BY  p.convocante ORDER BY monto_total DESC')
    print query


    cursor = connection.cursor()
    
  
    cursor.execute(query)
    result = dictfetchall(cursor)
    cursor.close()
    ret.put(result)
    return


def procedimiento(filtro, opcion,  anio, ret):
    query = ('SELECT  p.tipo_procedimiento, count(*) cantidad  '
            'FROM  openfonacide_planificacion p '             
            'WHERE p.etiquetas=\'fonacide\' AND  p.convocante  '+ opcion +
            'AND anio=\''+ anio + '\' '
            'GROUP BY  tipo_procedimiento ORDER BY cantidad DESC')
    print query


    cursor = connection.cursor()
    
  
    cursor.execute(query)
    result = dictfetchall(cursor)
    cursor.close()
    ret.put(result)
    return

def categoria(filtro, opcion, anio,  ret):
    query = ('SELECT  p.categoria, count(*) cantidad '
            'FROM  openfonacide_planificacion p '            
            'WHERE p.etiquetas=\'fonacide\' AND  p.convocante  '+ opcion + 
            'AND anio=\''+ anio + '\' '
            'GROUP BY  p.categoria ORDER BY cantidad DESC')
    print query

    cursor = connection.cursor()
    
  
    cursor.execute(query)
    result = dictfetchall(cursor)
    cursor.close()
    ret.put(result)
    return

