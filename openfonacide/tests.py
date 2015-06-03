# coding=utf-8
from django.test import TestCase

from openfonacide.models import Establecimiento
from openfonacide.utils import conversion
from openfonacide.matcher import token_compare, mismo_nivel_educativo, same_tipo_institucion, tiene_nombre_santo, \
    match_nombre_santo


class EstablecimientoTest(TestCase):
    def setUp(self):
        i = Establecimiento.objects.create(
            nombre="Institucion1",
            anio="2015",
            codigo_establecimiento="00112233"
        )
        i.save()

    def test_db_access(self):
        k = Establecimiento.objects.get(anio="2015")
        self.assertEqual(k.nombre, "Institucion1")
        self.assertEqual("00112233", k.codigo_establecimiento)
        self.assertEqual(None, k.fonacide)

    def test_unique_fields(self):
        try:
            nuevo_objeto = Establecimiento.objects.create(
                nombre="DifferentNameBut",
                anio="2015",
                codigo_establecimiento="00112233"
            )
            # Will never reach this point
        except Exception, e:
            # The message changes depending of the environment
            self.assertRegexpMatches(e.message,
                                     ".*UNIQUE constraint.*|columns anio, codigo_establecimiento are not unique")


def convert(test, iny, inx, outy, outx):
    ny = conversion(iny)
    nx = conversion(inx)
    test.assertEqual("%0.6f" % ny, outy)
    test.assertEqual("%0.6f" % nx, outx)


class UtilsTest(TestCase):
    def test_conversion_north_west(self):
        convert(self, u'40° 26\' 46" N', u'79° 58\' 56" W', '40.446111', '-79.982222')

    def test_conversion_nort_east(self):
        convert(self, u'30° N', u'20° E', '30.000000', '20.000000')

    def test_conversion_south_west(self):
        convert(self, u'30° S', u'10° 30\' W', '-30.000000', '-10.500000')

    def test_conversion_south_east(self):
        convert(self, u'100° 30\' S', u'10° 70\' E', '-100.500000', '11.166667')

    def test_conversion_cero(self):
        convert(self, u'0° N', u'0° N', '0.000000', '0.000000')

    def test_conversion_bad_input(self):
        convert(self, u'WERQ', u'TARE', '0.000000', '0.000000')


class MatcherTests(TestCase):
    def test_token_compare_true(self):
        c1 = u"THIS IS A STRING"
        c2 = u"THIS IS OTHER STRING"
        t = {u"THIS": 1, u"IS": 2, u"STRING": 4}
        self.assertTrue(token_compare(c1, c2, t))

    def test_token_compare_empty(self):
        c1 = u"ASDF"
        c2 = u"PORQ"
        t = {u"ZITH": 1}
        self.assertTrue(token_compare(c1, c2, t))

    def test_token_compare_false(self):
        c1 = u"THIS IS A"
        c2 = u"THIS IS B"
        t = {u"THIS": 1, u"B": 2}
        self.assertFalse(token_compare(c1, c2, t))

    def test_mismo_nivel_educativo(self):
        c1 = u"ESCUELA 1"
        c2 = u"ESCUELA 2"
        self.assertTrue(mismo_nivel_educativo(c1, c2))
        c1 = u"COLEGIO 1"
        c2 = u"COLEGIO 2"
        self.assertTrue(mismo_nivel_educativo(c1, c2))
        c1 = u"LICEO 1"
        c2 = u"LICEO 2"
        self.assertTrue(mismo_nivel_educativo(c1, c2))
        c1 = u"CENTRO 1"
        c2 = u"CENTRO 2"
        self.assertTrue(mismo_nivel_educativo(c1, c2))
        c1 = u"SEDE 1"
        c2 = u"SEDE 2"
        self.assertTrue(mismo_nivel_educativo(c1, c2))
        c1 = u"AULASALVAJE 1"
        c2 = u"AULASALVAJE 2"
        self.assertTrue(mismo_nivel_educativo(c1, c2))

    def test_mismo_nivel_educativo_multiple(self):
        c1 = u"ESCUELA COLEGIO LICEO 1"
        c2 = u"ESCUELA COLEGIO LICEO 2"
        self.assertTrue(mismo_nivel_educativo(c1, c2))
        c1 = u"ESCUELA COLEGIO LICEO SEDE 1"
        c2 = u"ESCUELA COLEGIO LICEO CENTRO 2"
        self.assertFalse(mismo_nivel_educativo(c1, c2))

    def test_mismo_nivel_educativo_empty(self):
        c1 = u"SIN NOMBRE"
        c2 = u""
        self.assertTrue(mismo_nivel_educativo(c1, c2))

    def test_mismo_nivel_educativo_false(self):
        c1 = u"COLEGIO CARLOS ANTONIO LOPEZ"
        c2 = u"LICEO CARLOS ANTONIO LOPEZ"
        self.assertFalse(mismo_nivel_educativo(c1, c2))

    def test_same_tipo_institucion_false(self):
        c1 = u"INSTITUTO PRIVADO"
        c2 = u"COLEGIO PUBLICO"
        self.assertFalse(same_tipo_institucion(c1, c2))

    def test_same_tipo_institucion_true(self):
        c1 = u"COLEGIO PRIVADO"
        c2 = u"INSTITUTO PRIVADO"
        self.assertTrue(same_tipo_institucion(c1, c2))
        c1 = u"ESCUELA PRIVADA 12321"
        c2 = u"ESCUELA2 PRIVADA 52134523"
        self.assertTrue(same_tipo_institucion(c1, c2))

    def tiene_nombre_santo(self):
        c1 = u"COLEGIO SAN LUCAS"
        c2 = u"COLEGIO SAN GERONIMO"
        self.assertEqual(tiene_nombre_santo(c1, c2), 1)
        c1 = u"COLEGIO SANTA LUCAS"
        c2 = u"COLEGIO SAN GERONIMO"
        self.assertEqual(tiene_nombre_santo(c1, c2), -2)
        c1 = u"COLEGIO LUCAS"
        c2 = u"COLEGIO GERONIMO"
        self.assertEqual(tiene_nombre_santo(c1, c2), -1)
        c1 = u"SAN SANTO UNO"
        c2 = u"SAN SANTO DOS"
        self.assertEqual(tiene_nombre_santo(c1, c2), 3)

    def match_nombre_santo(self):
        c1 = u"INSTITUTO SAN LUCAS"
        c2 = u"COLEGIO SAN LUCAS"
        self.assertTrue(match_nombre_santo(c1, c2, 1))
        c1 = u"SAN PEDRO"
        c2 = u"SAN PABLO"
        self.assertFalse(match_nombre_santo(c1, c2, 1))
