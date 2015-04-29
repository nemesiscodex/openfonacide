# coding=utf-8
from django.test import TestCase

from openfonacide.models import Establecimiento
from openfonacide.utils import conversion


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
            self.assertRegexpMatches(e.message, ".*UNIQUE constraint.*|columns anio, codigo_establecimiento are not unique")


def convert(test, iny, inx, outy, outx):
    ny = conversion(iny)
    nx = conversion(inx)
    test.assertEqual("%0.6f" % ny, outy)
    test.assertEqual("%0.6f" % nx, outx)

class UtilsTest(TestCase):
    def test_conversion_north_west(self):
        convert(self, u'40° 26\' 46" N', u'79° 58\' 56" W',  '40.446111',  '-79.982222')

    def test_conversion_nort_east(self):
        convert(self, u'30° N', u'20° E',  '30.000000',  '20.000000')

    def test_conversion_south_west(self):
        convert(self, u'30° S', u'10° 30\' W',  '-30.000000',  '-10.500000')

    def test_conversion_south_east(self):
        convert(self, u'100° 30\' S', u'10° 70\' E',  '-100.500000',  '11.166667')

    def test_conversion_cero(self):
        convert(self, u'0° N', u'0° N',  '0.000000',  '0.000000')

    def test_conversion_bad_input(self):
        convert(self, u'WERQ', u'TARE',  '0.000000',  '0.000000')
