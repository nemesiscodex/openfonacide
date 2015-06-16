# coding=utf-8
from psycopg2.extensions import adapt


def conversion(dms):
    """
    Convierte coordenadas DMS a decimales
    :param DMS:
    :return:
    """
    direction = {'N': 1, 'S': -1, 'E': 1, 'W': -1}
    decimal = dms.replace(u'°', ' ').replace('\'', ' ').replace('"', ' ').replace('\\', ' ')
    decimal = decimal.split()
    decimal_dir = decimal.pop()
    decimal.extend([0, 0, 0])
    if decimal_dir not in ['N', 'S', 'E', 'W']:
        return 0
    return (float(decimal[0]) + float(decimal[1]) / 60.0 + float(decimal[2]) / 3600.0) * direction[decimal_dir]


def dictfetch(cursor, N, offset=None):
    """Returns all rows from a cursor as a dict"""
    desc = cursor.description
    rows = []

    try:
        N = int(N)
    except:
        N = None
    if not N:
        rows = cursor.fetchall()
    else:
        try:
            offset = int(offset)
        except:
            pass
        if offset and type(offset) == int:
            N = offset + N
        else:
            offset = 0
        rows = cursor.fetchall()[offset:N]
    return [
        dict(zip([col[0] for col in desc], row))
        for row in rows
        ]


def escapelike(query):
    result = adapt(query).__str__()
    return result[1:len(result) - 1]
