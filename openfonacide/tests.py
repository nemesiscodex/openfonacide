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
            self.assertRegexpMatches(e.message, "columns anio, codigo_establecimiento are not unique")


class UtilsTest(TestCase):
    def test_conversion_north_west(self):
        y = u'40° 26\' 46" N'
        x = u'79° 58\' 56" W'
        ny = conversion(y)
        nx = conversion(x)
        self.assertEqual("%0.6f" % ny, '40.446111')
        self.assertEqual("%0.6f" % nx, '-79.982222')

    def test_conversion_nort_east(self):
        y = u'30° N'
        x = u'20° E'
        ny = conversion(y)
        nx = conversion(x)
        self.assertEqual("%0.6f" % ny, '30.000000')
        self.assertEqual("%0.6f" % nx, '20.000000')

    def test_conversion_south_west(self):
        y = u'30° S'
        x = u'10° 30\' W'
        ny = conversion(y)
        nx = conversion(x)
        self.assertEqual("%0.6f" % ny, '-30.000000')
        self.assertEqual("%0.6f" % nx, '-10.500000')

    def test_conversion_south_east(self):
        y = u'100° 30\' S'
        x = u'10° 70\' E'
        ny = conversion(y)
        nx = conversion(x)
        self.assertEqual("%0.6f" % ny, '-100.500000')
        self.assertEqual("%0.6f" % nx, '11.166667')

    def test_conversion_cero(self):
        y = u'0° N'
        x = u'0° N'
        ny = conversion(y)
        nx = conversion(x)
        self.assertEqual("%0.6f" % ny, '0.000000')
        self.assertEqual("%0.6f" % nx, '0.000000')

    def test_conversion_bad_input(self):
        y = u'WERQ'
        x = u'TARE'
        ny = conversion(y)
        nx = conversion(x)
        self.assertEqual("%0.6f" % ny, '0.000000')
        self.assertEqual("%0.6f" % nx, '0.000000')