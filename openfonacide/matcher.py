# encoding: utf-8
import os
from fuzzywuzzy import fuzz
from django.db.models import Q

__author__ = 'synchro'

"""
    Esta es una reimplementación del en python del código
    de Lilian Nieto, publicado en github
    https://github.com/sgip/MacheoNombresInstituciones/
    Esta es una linea de atribución y agradecimiento a su trabajo
"""

import string
import re
from nltk import metrics


class Matcher(object):
    """
    Esta Clase implementa los métodos para facilitar la comparación difusa
    entre Nombres de instituciones del MEC y la descripción de los llamados
    de la DNCP

    http://datos.mec.gov.py/data/directorios_instituciones

    https://www.contrataciones.gov.py/datos/data

    """

    @staticmethod
    def normalizar_string(cadena):
        assert isinstance(cadena, unicode)
        normalizada = cadena.upper()

        normalizada = normalizada.replace(u'Á', 'A')
        normalizada = normalizada.replace(u'É', 'E')
        normalizada = normalizada.replace(u'Í', 'I')
        normalizada = normalizada.replace(u'Ó', 'O')
        normalizada = normalizada.replace(u'Ú', 'U')
        normalizada = normalizada.replace(u'Ñ', 'N')
        # Error usual encontrado en los datasets
        normalizada = normalizada.replace(u'Ń', 'N')
        # Eliminar Stop Words
        normalizada = remove_stop_words(normalizada)

        # Reemplazo de las abreviaciones usuales
        normalizada = normalizada.replace('ESC.', 'ESCUELA')
        normalizada = normalizada.replace('ESC ', 'ESCUELA ')
        normalizada = normalizada.replace('BAS.', 'BASICA')
        normalizada = normalizada.replace('BAS ', 'BASICA ')
        normalizada = normalizada.replace('COL.', 'COLEGIO')
        normalizada = normalizada.replace('COL ', 'COLEGIO ')
        normalizada = normalizada.replace('NAC.', 'NACIONAL')
        normalizada = normalizada.replace('NAC ', 'NACIONAL ')
        normalizada = normalizada.replace('TEC.', 'TECNICO')
        normalizada = normalizada.replace('TEC ', 'TECNICO ')
        normalizada = normalizada.replace('PARROQ.', 'PARROQUIAL')
        normalizada = normalizada.replace('PARROQ ', 'PARROQUIAL ')
        normalizada = normalizada.replace('PRIV.', 'PRIVADO')
        normalizada = normalizada.replace('PRIV ', 'PRIVADO ')
        normalizada = normalizada.replace('SUBV.', 'SUBVENCIONADO')
        normalizada = normalizada.replace('SUBV ', 'SUBVENCIONADO ')
        normalizada = normalizada.replace('TEC ', 'TECNICO ')
        normalizada = normalizada.replace('LIC.', 'LICEO')
        normalizada = normalizada.replace('LIC ', 'LICEO ')
        normalizada = normalizada.replace('I. F. D. ', 'INSTITUTO FORMACION DOCENTE')
        normalizada = normalizada.replace('GRAL.', 'GENERAL')
        normalizada = normalizada.replace('GRAL ', 'GENERAL ')
        normalizada = normalizada.replace('PROF.', 'PROFESOR')
        normalizada = normalizada.replace('PROF ', 'PROFESOR ')
        normalizada = normalizada.replace('RCA.', 'REPUBLICA')
        normalizada = normalizada.replace('RCA ', 'REPUBLICA')
        normalizada = normalizada.replace('MCAL.', 'MARISCAL')
        normalizada = normalizada.replace('MCAL ', 'MARISCAL ')
        normalizada = normalizada.replace('CPTAN.', 'CAPITAN')
        normalizada = normalizada.replace('CPTAN ', 'CAPITAN ')
        normalizada = normalizada.replace('TTE.', 'TETIENTE')
        normalizada = normalizada.replace('TTE ', 'TETIENTE ')
        normalizada = normalizada.replace('DR.', 'DOCTOR')
        normalizada = normalizada.replace('DR ', 'DOCTOR ')
        normalizada = normalizada.replace('PDTE.', 'PRESIDENTE')
        normalizada = normalizada.replace('PDTE ', 'PRESIDENTE ')
        normalizada = normalizada.replace('STA.', 'SANTA')
        normalizada = normalizada.replace('STA ', 'SANTA ')
        normalizada = normalizada.replace('NTRA.', 'NUESTRA')
        normalizada = normalizada.replace('PARROQ.', 'PARROQUIAL')
        normalizada = normalizada.replace('PARROQ ', 'PARROQUIAL')
        normalizada = normalizada.replace('E.M.A.', 'EDUCACION MEDIA ABIERTA')
        normalizada = normalizada.replace('EMA', 'EDUCACION MEDIA ABIERTA ')
        normalizada = normalizada.replace('C.R.E.P.', 'CENTRO REGIONAL DE EDUCACION PILAR')
        normalizada = normalizada.replace('CREP ', 'CENTRO REGIONAL DE EDUCACION PILAR ')
        normalizada = normalizada.replace('AVDA ', 'AVENIDA ')
        normalizada = normalizada.replace('AVDA.', 'AVENIDA')

        # Reemplaza puntución por espacio
        for p in string.punctuation:
            normalizada = normalizada.replace(p, ' ')

        normalizada = re.sub('\s+DEL ', ' ', normalizada)
        normalizada = re.sub('\s+EL ', ' ', normalizada)
        normalizada = re.sub('\s+LA ', ' ', normalizada)
        normalizada = re.sub('\s+PARA ', ' ', normalizada)
        normalizada = re.sub('\s+Y ', ' ', normalizada)


        # Eliminar espacios repetidos
        normalizada = re.sub('\s+', ' ', normalizada)
        normalizada = normalizada.strip()

        # if normalizada == "":
        # normalizada = None

        return normalizada

    @staticmethod
    def heuristicas(cadena1, cadena2):
        assert isinstance(cadena1, unicode)
        assert isinstance(cadena2, unicode)
        # Verificar si son
        # ESCUELA
        # COLEGIO
        # LICEO
        # CENTRO
        # SEDE

        if not mismo_nivel_educativo(cadena1, cadena2):
            return False

        # Verificar si las instituciones son Públicas o Privadas
        if not same_tipo_institucion(cadena1, cadena2):
            return False

        pos_nombre = tiene_nombre_santo(cadena1, cadena2)
        if pos_nombre > 0:
            if match_nombre_santo(cadena1, cadena2, pos_nombre):
                # Validadas cadenas con nombres de santos
                print(cadena1 + ' is ok')
                return True
            else:
                return False
        elif pos_nombre < -1:
            return False

        # t_value = fuzz.partial_ratio(cadena1, cadena2)
        # t_value = fuzz.partial_token_set_ratio(cadena1, cadena2)
        t_value = fuzz.token_set_ratio(cadena1, cadena2)
        if t_value >= 70:
            print("[matcher] (" + cadena1 + " , " + cadena2 + ") = " + str(t_value))
            return True
        else:
            return False



            # Deprecated in favor of fuzzywuzzy
            # Aplicar distancia de Damerau-Levenshtein
            # editdistance = metrics.edit_distance(cadena1, cadena2)
            # max_longitud = float(len(max(cadena1, cadena2)))
            # if editdistance > (0.3 * max_longitud):
            # return False
            # else:
            # # Match
            #    print(cadena1 + ' is OK')
            #    return True

    @staticmethod
    def do_match(institucion_manager=None, planificacion_manager=None, temporal_manager=None):
        inst = institucion_manager.all()
        total_instituciones = str(len(inst))
        print("Se tienen " + total_instituciones + " instituciones")
        planes = planificacion_manager.filter(etiquetas__icontains="fonacide")
        total_planificaciones = str(len(planes))
        print("Se filtraron " + total_planificaciones + " planificaciones")
        res = ""
        time = 0
        match = 0
        institucion_actual = 0
        for i in inst:
            institucion_actual += 1
            # print("BEGIN Executing OR-Query!")
            planes_for_match = planes.filter(
                Q(convocante__icontains=i.nombre_distrito) | Q(convocante__icontains=i.nombre_departamento))
            planificaciones_candidatas = str(len(planes_for_match))
            # print("END Executing OR-Query!")

            #print("[" + i.nombre_institucion + "] existen " + str(len(
            #    planes_for_match)) + " por (" + i.nombre_departamento + " | " + i.nombre_distrito + ") en convocante")

            plan_actual = 0
            for j in planes_for_match:
                time += 1
                plan_actual += 1
                #print(str(time) + " " + i.nombre_institucion + " _ " + j.nombre_licitacion)
                ti = Matcher.normalizar_string(i.nombre_institucion)
                tj = Matcher.normalizar_string(j.nombre_licitacion)
                res = res + "<p> |" + ti + " _ " + tj + "| </p>"

                if Matcher.heuristicas(ti, tj):
                    match += 1
                    temp = temporal_manager.create(periodo=i.periodo, nombre_departamento=i.nombre_departamento,
                                                   nombre_distrito=i.nombre_distrito,
                                                   codigo_institucion=i.codigo_institucion,
                                                   nombre_institucion=i.nombre_institucion,
                                                   id_planificacion=j.id, anio=j.anio,
                                                   id_llamado=j.id_llamado, nombre_licitacion=j.nombre_licitacion,
                                                   convocante=j.convocante)

                    #print(
                    #    "[" + str(match) + "/" + str(
                    #        time) + "] (" + i.nombre_institucion + " , " + j.nombre_licitacion + ")")
                    print(
                        "[" + str(institucion_actual) + "/" + str(total_instituciones) + "][" + str(
                            plan_actual) + "/" + str(planificaciones_candidatas) + "/" + str(
                            total_planificaciones) + "]")

        return {'resultados': res, 'time': time}


def mismo_nivel_educativo(c1, c2):
    """
    Verifica que las dos cadenas tengan nombres de instituciones
    del mismo nivel educativo

    :param c1,c2  Cadenas a verificar si tienen el mismo nivel educativo

    Se verifica que si, por ejemplo c1 contiene la palabra ESCUELA, entonces
    c2 debe tener tambien la misma palabra, de lo contrario compararíamos
    institutos de distinto nivel académico y por tanto diferentes por lo que ya
    se puede decir con seguridad que no son la misma institucion

    Los Niveles son
    - ESCUELA
    - COLEGIO
    - LICEO
    - CENTRO
    - SEDE
    """
    niveles = {"ESCUELA": 1, "COLEGIO": 2, "LICEO": 4, "CENTRO": 8, "SEDE": 16}

    assert isinstance(c1, unicode)
    assert isinstance(c1, unicode)

    return token_compare(c1, c2, niveles)


def same_tipo_institucion(c1, c2):
    """
    Verifica ambas cadenas hagan referencia a instituciones
    O bien ambas Públicas o bien ambas privadas

    """
    # Ver los casos donde los géneros son diferentes "PRIVADO", "PUBLICO"
    tipos = {"PRIVADA": 1, "PUBLICA": 2, "PRIVADO": 4, "PUBLICO": 8}

    assert isinstance(c1, unicode)
    assert isinstance(c1, unicode)

    return token_compare(c1, c2, tipos)


def token_compare(c1, c2, token_dict):
    """
    Verifica que dos cadenas tengan ambas ciertos tokens dados por los elementos
    en el diccionario :param token_dict

    Retorna True si ambas cadenas tienen ciertos tokens, o no los tienen en absoluto
    Retorna False si una cadena tiene uno de los tokens diferente de la otra
    """
    k1 = 0
    k2 = 0

    for i, j in token_dict.items():
        if c1.find(i) >= 0:
            k1 += j

        if c2.find(i) >= 0:
            k2 += j

    return k1 == k2


def tiene_nombre_santo(c1, c2):
    """
    Verificar si c1 o c2 tiene las palabras
    SAN, SANTA o SANTO, ambos

    :param c1: Cadena 1
    :param c2: Cadena 2
    :return: -1 si no tiene ninguno de los valores SAN, SANTO o SANTA
    :type c1: str
    :type c2: str
    """

    tipos = {"SAN ": 1, "SANTO ": 2, "SANTA ": 4}

    assert isinstance(c1, unicode)
    assert isinstance(c1, unicode)

    k1 = 0
    k2 = 0

    for i, j in tipos.items():
        if c1.find(i) >= 0:
            k1 += j

        if c2.find(i) >= 0:
            k2 += j

    if k1 == k2 and k1 == 0:
        return -1
    if k1 == k2 and k1 != 0:
        return k1
    return -2  # No se puede Matchear


def match_nombre_santo(c1, c2, pos):
    tipos = {1: 'SAN ', 2: 'SANTA ', 4: 'SANTO '}
    n = c1.find(tipos[pos])
    nombre1 = c1[n + len(tipos[pos]):]
    n = c2.find(tipos[pos])
    nombre2 = c2[n + len(tipos[pos]):]

    if nombre1 == nombre2:
        return True
    else:
        editdistance = metrics.edit_distance(nombre1, nombre2)
        return editdistance <= (0.1 * len(max(nombre1, nombre2)).__float__())


def remove_stop_words(normalizada=None, file_name='palabrasDNCP.txt'):
    # Initialize STOP-WORDS source
    # XXX: Could be improved, by using some global data source for
    # Stop-Words
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, file_name)
    sw_file = open(file_path)

    stop_words = list()

    for sw in sw_file.readlines():
        sw.replace('\n', '')
        stop_words.append(sw.upper())

    sw_file.close()

    for k in stop_words:
        normalizada.replace(k, '')

    return normalizada