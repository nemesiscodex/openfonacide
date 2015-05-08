import json
from django.db import connection
from openfonacide.views import JSONResponse


def filtros(request):
    nombre = request.GET.get('f')
    if nombre == 'fonacide':
        # print type(filtro_fonacide())
        # print filtro_fonacide()
        return JSONResponse(json.loads(filtro_fonacide()))
    else:
        return JSONResponse('[]')


def filtro_fonacide():
    cursor = connection.cursor()
    cursor.execute('SELECT DISTINCT codigo_establecimiento FROM '
                    '(SELECT DISTINCT es.codigo_establecimiento codigo_establecimiento, '
                    'p_es.periodo periodo FROM openfonacide_establecimiento es '
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
