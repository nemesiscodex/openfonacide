# coding=utf-8
from django.test import TestCase
from openfonacide.models import Institucion
from openfonacide.utils import conversion

class InstitucionTest(TestCase):
    def setUp(self):
        i = Institucion.objects.create(nombre="Institucion1",anio="2015")
        i.save()
		
    def test_db_access(self):
        k = Institucion.objects.get(anio="2015")
        self.assertEqual(k.nombre,"Institucion1")


class UtilsTest(TestCase):
    def test_conversion_north_west(self):
        y = u'40° 26\' 46" N'
        x = u'79° 58\' 56" W'
        ny = conversion(y)
        nx = conversion(x)
        self.assertEqual("%0.6f"%ny,'40.446111')
        self.assertEqual("%0.6f"%nx,'-79.982222')

    def test_conversion_nort_east(self):
        y = u'30° N'
        x = u'20° E'
        ny = conversion(y)
        nx = conversion(x)
        self.assertEqual("%0.6f"%ny,'30.000000')
        self.assertEqual("%0.6f"%nx,'20.000000')

    def test_conversion_south_west(self):
        y = u'30° S'
        x = u'10° 30\' W'
        ny = conversion(y)
        nx = conversion(x)
        self.assertEqual("%0.6f"%ny,'-30.000000')
        self.assertEqual("%0.6f"%nx,'-10.500000')

    def test_conversion_south_east(self):
        y = u'100° 30\' S'
        x = u'10° 70\' E'
        ny = conversion(y)
        nx = conversion(x)
        self.assertEqual("%0.6f"%ny,'-100.500000')
        self.assertEqual("%0.6f"%nx,'11.166667')

    def test_conversion_cero(self):
        y = u'0° N'
        x = u'0° N'
        ny = conversion(y)
        nx = conversion(x)
        self.assertEqual("%0.6f"%ny, '0.000000')
        self.assertEqual("%0.6f"%nx, '0.000000')
