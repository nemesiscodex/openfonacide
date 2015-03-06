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
		
		
