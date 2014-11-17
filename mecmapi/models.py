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
    nombre = models.CharField(max_length=256, default='<Sin nombre>')


class InstitucionData(models.Model):
    anio = models.CharField(max_length=128)
    codigo_departamento = models.CharField(max_length=128)
    nombre_departamento = models.CharField(max_length=128)
    codigo_distrito = models.CharField(max_length=128)
    nombre_distrito = models.CharField(max_length=128)
    codigo_barrio_localidad = models.CharField(max_length=128)
    nombre_barrio_localidad = models.CharField(max_length=128)
    codigo_zona = models.CharField(max_length=128)
    nombre_zona = models.CharField(max_length=128)
    codigo_establecimiento = models.ForeignKey('Institucion')
    codigo_institucion = models.CharField(max_length=128)
    nombre_institucion = models.CharField(max_length=128)
    sector_o_tipo_gestion = models.CharField(max_length=128)
    codigo_region_administrativa = models.CharField(max_length=128)
    nombre_region_administrativa = models.CharField(max_length=128)
    nombre_supervisor = models.CharField(max_length=128)
    niveles_modalidades = models.CharField(max_length=128)
    codigo_tipo_organizacion = models.CharField(max_length=128)
    nombre_tipo_organizacion = models.CharField(max_length=128)
    participacion_comunitaria = models.CharField(max_length=128)
    direccion = models.CharField(max_length=128)
    nro_telefono = models.CharField(max_length=128)
    tiene_internet = models.CharField(max_length=128)
    paginaweb = models.CharField(max_length=128)
    correo_electronico = models.CharField(max_length=128)
