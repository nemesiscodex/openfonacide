# coding=utf-8


def conversion(old):
    """
    Convierte coordenadas DMS a decimales
    :param old:
    :return:
    """
    direction = {'N': 1, 'S': -1, 'E': 1, 'W': -1}
    new = old.replace(u'°', ' ').replace('\'', ' ').replace('"', ' ')
    new = new.split()
    new_dir = new.pop()
    new.extend([0, 0, 0])
    return (float(new[0]) + float(new[1]) / 60.0 + float(new[2]) / 3600.0) * direction[new_dir]
