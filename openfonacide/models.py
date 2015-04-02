# encoding: utf-8
"""
Open data mec map api models
"""

from django.db import models


class Establecimiento(models.Model):
    """
    Modelo de datos que representa los Establecimientos
    """
    anio = models.CharField(max_length=256)
    codigo_establecimiento = models.CharField(max_length=256, primary_key=True)
    codigo_departamento = models.CharField(max_length=256)
    nombre_departamento = models.CharField(max_length=256)
    codigo_distrito = models.CharField(max_length=256)
    nombre_distrito = models.CharField(max_length=256)
    codigo_zona = models.CharField(max_length=256)
    nombre_zona = models.CharField(max_length=256)
    codigo_barrio_localidad = models.CharField(max_length=256)
    nombre_barrio_localidad = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)
    coordenadas_y = models.CharField(max_length=256)
    coordenadas_x = models.CharField(max_length=256)
    latitud = models.CharField(max_length=256)
    longitud = models.CharField(max_length=256)
    anho_cod_geo = models.CharField(max_length=256)
    uri = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256, default='<Sin nombre>')
    fonacide = models.CharField(max_length=5, null=True)


# Datos Específicos de Instituciones Educativas
class InstitucionData(models.Model):
    anio = models.CharField(max_length=256)
    codigo_departamento = models.CharField(max_length=256)
    nombre_departamento = models.CharField(max_length=256)
    codigo_distrito = models.CharField(max_length=256)
    nombre_distrito = models.CharField(max_length=256)
    codigo_barrio_localidad = models.CharField(max_length=256)
    nombre_barrio_localidad = models.CharField(max_length=256)
    codigo_zona = models.CharField(max_length=256)
    nombre_zona = models.CharField(max_length=256)
    codigo_establecimiento = models.ForeignKey('Establecimiento')
    codigo_institucion = models.CharField(max_length=256)
    nombre_institucion = models.CharField(max_length=256)
    sector_o_tipo_gestion = models.CharField(max_length=256)
    codigo_region_administrativa = models.CharField(max_length=256)
    nombre_region_administrativa = models.CharField(max_length=256)
    nombre_supervisor = models.CharField(max_length=256)
    niveles_modalidades = models.CharField(max_length=256)
    codigo_tipo_organizacion = models.CharField(max_length=256)
    nombre_tipo_organizacion = models.CharField(max_length=256)
    participacion_comunitaria = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)
    nro_telefono = models.CharField(max_length=256)
    tiene_internet = models.CharField(max_length=256)
    paginaweb = models.CharField(max_length=256)
    correo_electronico = models.CharField(max_length=256)


# Prioridades 2.0###############################################################################
# En este modelo se representan los datasets de Aluas y Otros Espacios
# por que solo difieren en el valor del campo espacio_destinado
class Espacios(models.Model):
    periodo = models.CharField(max_length=50, null=True)
    cod_departamento = models.CharField(max_length=256, null=True)
    nombre_departamento = models.CharField(max_length=256, null=True)
    cod_distrito = models.CharField(max_length=256, null=True)
    nombre_distrito = models.CharField(max_length=200, null=True)
    prioridad = models.IntegerField(null=True)
    cod_establecimiento = models.CharField(max_length=256, null=True)
    cod_institucion = models.CharField(max_length=256, null=True)
    nombre_institucion = models.CharField(max_length=200)
    codigo_zona = models.CharField(max_length=256, null=True)
    nombre_zona = models.CharField(max_length=256, null=True)
    nivel_educativo_beneficiado = models.CharField(max_length=256, null=True)
    cuenta_con_espacio_construccion = models.CharField(max_length=256, null=True)
    espacio_destinado = models.CharField(max_length=200, null=True)
    tipo_requerimiento_infraestructura = models.CharField(max_length=200, null=True)
    cantidad_requerida = models.CharField(max_length=256, null=True)
    numero_beneficiados = models.CharField(max_length=256, null=True)
    justificacion = models.CharField(max_length=900, null=True)
    uri_establecimiento = models.CharField(max_length=256, null=True)
    uri_institucion = models.CharField(max_length=256, null=True)


class Sanitarios(models.Model):
    periodo = models.CharField(max_length=50, null=True)
    cod_departamento = models.CharField(max_length=256, null=True)
    nombre_departamento = models.CharField(max_length=256, null=True)
    cod_distrito = models.CharField(max_length=256, null=True)
    nombre_distrito = models.CharField(max_length=200, null=True)
    prioridad = models.IntegerField(null=True)
    cod_establecimiento = models.CharField(max_length=256, null=True)
    cod_institucion = models.CharField(max_length=256, null=True)
    nombre_institucion = models.CharField(max_length=200, null=True)
    codigo_zona = models.CharField(max_length=256, null=True)
    nombre_zona = models.CharField(max_length=256, null=True)
    nivel_educativo_beneficiado = models.CharField(max_length=256, null=True)
    abastecimiento_agua = models.CharField(max_length=256, null=True)
    servicio_sanitario_actual = models.CharField(max_length=256, null=True)
    cuenta_con_espacio_construccion = models.CharField(max_length=256, null=True)
    tipo_requerimiento_infraestructura = models.CharField(max_length=200, null=True)
    cantidad_requerida = models.CharField(max_length=256, null=True)
    numero_beneficiados = models.CharField(max_length=256, null=True)
    justificacion = models.CharField(max_length=900, null=True)
    uri_establecimiento = models.CharField(max_length=256, null=True)
    uri_institucion = models.CharField(max_length=256, null=True)


class Mobiliarios(models.Model):
    periodo = models.CharField(max_length=50, null=True)
    cod_departamento = models.CharField(max_length=256, null=True)
    nombre_departamento = models.CharField(max_length=256, null=True)
    cod_distrito = models.CharField(max_length=256, null=True)
    nombre_distrito = models.CharField(max_length=200, null=True)
    prioridad = models.IntegerField(null=True)
    cod_establecimiento = models.CharField(max_length=256, null=True)
    cod_institucion = models.CharField(max_length=256, null=True)
    nombre_institucion = models.CharField(max_length=200, null=True)
    codigo_zona = models.CharField(max_length=256, null=True)
    nombre_zona = models.CharField(max_length=256, null=True)
    nivel_educativo_beneficiado = models.CharField(max_length=256, null=True)
    nombre_mobiliario = models.CharField(max_length=256, null=True)
    cantidad_requerida = models.CharField(max_length=256, null=True)
    numero_beneficiados = models.CharField(max_length=256, null=True)
    justificacion = models.CharField(max_length=1200, null=True)
    uri_establecimiento = models.CharField(max_length=256, null=True)
    uri_institucion = models.CharField(max_length=256, null=True)


# Servicios Básicos de los establecimientos según fonacide
class EstadosLocales(models.Model):
    periodo = models.CharField(max_length=50, null=True)
    cod_departamento = models.CharField(max_length=256, null=True)
    nombre_departamento = models.CharField(max_length=256, null=True)
    cod_distrito = models.CharField(max_length=256, null=True)
    nombre_distrito = models.CharField(max_length=200, null=True)
    cod_establecimiento = models.CharField(max_length=200, null=True)
    codigo_barrio_localidad = models.CharField(max_length=200, null=True)
    nombre_barrio_localidad = models.CharField(max_length=200, null=True)
    codigo_zona = models.CharField(max_length=256, null=True)
    nombre_zona = models.CharField(max_length=256, null=True)
    nombre_asentamiento_colonia = models.CharField(max_length=256, null=True)
    suministro_energia_electrica = models.CharField(max_length=256, null=True)
    abastecimiento_agua = models.CharField(max_length=256, null=True)
    servicio_sanitario_actual = models.CharField(max_length=256, null=True)
    titulo_de_propiedad = models.CharField(max_length=256, null=True)
    cuenta_plano = models.CharField(max_length=256, null=True)
    prevencion_incendio = models.CharField(max_length=256, null=True)
    uri_establecimiento = models.CharField(max_length=256, null=True)

