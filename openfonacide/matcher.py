# encoding: utf-8
__author__ = 'synchro'

"""
    Esta es una reimplementación del en python del código
    de Lilian Nieto, publicado en github
    https://github.com/sgip/MacheoNombresInstituciones/
    Esta es una linea de atribución y agradecimiento a su trabajo
"""

import string
import re


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
        assert isinstance(cadena, str)
        normalizada = cadena.strip()
        normalizada = normalizada.upper()
        normalizada = normalizada.replace('Á', 'A')
        normalizada = normalizada.replace('É', 'E')
        normalizada = normalizada.replace('Í', 'I')
        normalizada = normalizada.replace('Ó', 'O')
        normalizada = normalizada.replace('Ú', 'U')
        normalizada = normalizada.replace('Ñ', 'N')

        for p in string.punctuation:
            normalizada = normalizada.replace(p, '')

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
        normalizada = normalizada.replace('MCAL.', 'MARISCAL')
        normalizada = normalizada.replace('MCAL ', 'MARISCAL ')
        normalizada = normalizada.replace('CPTAN.', 'CAPITAN')
        normalizada = normalizada.replace('CPTAN ', 'CAPITAN ')
        normalizada = normalizada.replace('DR.', 'DOCTOR')
        normalizada = normalizada.replace('DR ', 'DOCTOR ')
        normalizada = normalizada.replace('STA.', 'SANTA')
        normalizada = normalizada.replace('STA ', 'SANTA ')

        # Eliminar espacios repetidos
        normalizada = re.sub('\s+', ' ', normalizada)

        if normalizada == "":
            normalizada = None

        return normalizada

    @staticmethod
    def heuristicas(cadena1, cadena2):
        assert isinstance(cadena1, str)
        assert isinstance(cadena2, str)

        # Verificar si son
        # ESCUELA
        # COLEGIO
        # LICEO
        # CENTRO
        # SEDE

        if not mismo_nivel_educativo(cadena1, cadena2):
            return

        # Verificar si las instituciones son Públicas o Privadas
        if not same_tipo_institucion(cadena1, cadena2):
            return


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

    assert isinstance(c1, str)
    assert isinstance(c1, str)

    return token_compare(c1, c2, niveles)


def same_tipo_institucion(c1, c2):
    """
    Verifica ambas cadenas hagan referencia a instituciones
    O bien ambas Públicas o bien ambas privadas

    """
    # Ver los casos donde los géneros son diferentes "PRIVADO", "PUBLICO"
    tipos = {"PRIVADA": 1, "PUBLICA": 2}

    assert isinstance(c1, str)
    assert isinstance(c1, str)

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