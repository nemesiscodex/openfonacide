# coding=utf-8


def conversion(dms):
    """
    Convierte coordenadas DMS a decimales
    :param DMS:
    :return:
    """
    direction = {'N': 1, 'S': -1, 'E': 1, 'W': -1}
    decimal = dms.replace(u'°', ' ').replace('\'', ' ').replace('"', ' ')
    decimal = decimal.split()
    decimal_dir = decimal.pop()
    decimal.extend([0, 0, 0])
    return (float(decimal[0]) + float(decimal[1]) / 60.0 + float(decimal[2]) / 3600.0) * direction[decimal_dir]
