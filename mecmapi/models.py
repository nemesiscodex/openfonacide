"""
Open data mec map api models
"""

from django.db import models

class Institucion(models.Model):
    anio = models.CharField(max_length=128)
    codigo_establecimiento = models.CharField(max_length=128, primary_key=True)
    codigo_departamento = models.CharField(max_length=128)
    nombre_departamento = models.CharField(max_length=128)
    codigo_distrito = models.CharField(max_length=128)
    nombre_distrito = models.CharField(max_length=128)
    codigo_zona = models.CharField(max_length=128)
    nombre_zona = models.CharField(max_length=128)
    codigo_barrio_localidad = models.CharField(max_length=128)
    nombre_barrio_localidad = models.CharField(max_length=128)
    direccion = models.CharField(max_length=128)
    coordenadas_y = models.CharField(max_length=128)
    coordenadas_x = models.CharField(max_length=128)
    latitud = models.CharField(max_length=128)
    longitud = models.CharField(max_length=128)
    anho_cod_geo = models.CharField(max_length=128)
    programa = models.CharField(max_length=128)
    proyecto_111 = models.CharField(max_length=128)
    proyecto_822 = models.CharField(max_length=128)
    uri = models.CharField(max_length=128)