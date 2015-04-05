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
    codigo_establecimiento = models.CharField(max_length=256)
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
    # Nombre corresponde a la concatenacion de los nombres de instituciones
    # dentro de el establecimiento
    nombre = models.CharField(max_length=256, default='<Sin nombre>')
    # Fonacide es una variable calculada, correspondiente a si esta en una lista de prioridades
    fonacide = models.CharField(max_length=5, null=True)

    class Meta:
        unique_together = (("anio", "codigo_establecimiento"),)


# Datos Específicos de Instituciones Educativas
class Institucion(models.Model):
    periodo = models.CharField(max_length=256)
    codigo_departamento = models.CharField(max_length=256)
    nombre_departamento = models.CharField(max_length=256)
    codigo_distrito = models.CharField(max_length=256)
    nombre_distrito = models.CharField(max_length=256)
    codigo_barrio_localidad = models.CharField(max_length=256)
    nombre_barrio_localidad = models.CharField(max_length=256)
    codigo_zona = models.CharField(max_length=256)
    nombre_zona = models.CharField(max_length=256)
    codigo_establecimiento = models.CharField(max_length=256)
    codigo_institucion = models.CharField(max_length=256)
    nombre_institucion = models.CharField(max_length=256)
    anho_cod_geo = models.CharField(max_length=256)
    uri_establecimiento = models.CharField(max_length=256, null=True)
    uri_institucion = models.CharField(max_length=256, null=True)

    class Meta:
        verbose_name_plural = "instituciones"

    # Estos campos no aparecen en la nueva version

    # sector_o_tipo_gestion = models.CharField(max_length=256)
    # codigo_region_administrativa = models.CharField(max_length=256)
    # nombre_region_administrativa = models.CharField(max_length=256)
    # nombre_supervisor = models.CharField(max_length=256)
    # niveles_modalidades = models.CharField(max_length=256)
    # codigo_tipo_organizacion = models.CharField(max_length=256)
    # nombre_tipo_organizacion = models.CharField(max_length=256)
    # participacion_comunitaria = models.CharField(max_length=256)
    # direccion = models.CharField(max_length=256)
    # nro_telefono = models.CharField(max_length=256)
    # tiene_internet = models.CharField(max_length=256)
    # paginaweb = models.CharField(max_length=256)
    # correo_electronico = models.CharField(max_length=256)


# Prioridades 2.0###############################################################################
# En este modelo se representan los datasets de Aluas y Otros Espacios
# por que solo difieren en el valor del campo espacio_destinado
class Espacio(models.Model):
    periodo = models.CharField(max_length=50, null=True)
    codigo_departamento = models.CharField(max_length=256, null=True)
    nombre_departamento = models.CharField(max_length=256, null=True)
    codigo_distrito = models.CharField(max_length=256, null=True)
    nombre_distrito = models.CharField(max_length=200, null=True)
    numero_prioridad = models.IntegerField(null=True)
    codigo_establecimiento = models.CharField(max_length=256, null=True)
    codigo_institucion = models.CharField(max_length=256, null=True)
    nombre_institucion = models.CharField(max_length=200)
    codigo_zona = models.CharField(max_length=256, null=True)
    nombre_zona = models.CharField(max_length=256, null=True)
    nivel_educativo_beneficiado = models.CharField(max_length=256, null=True)
    cuenta_espacio_para_construccion = models.CharField(max_length=256, null=True)
    nombre_espacio = models.CharField(max_length=200, null=True)
    tipo_requerimiento_infraestructura = models.CharField(max_length=200, null=True)
    cantidad_requerida = models.CharField(max_length=256, null=True)
    numero_beneficiados = models.CharField(max_length=256, null=True)
    justificacion = models.CharField(max_length=2048, null=True)
    uri_establecimiento = models.CharField(max_length=256, null=True)
    uri_institucion = models.CharField(max_length=256, null=True)


class Sanitario(models.Model):
    periodo = models.CharField(max_length=50, null=True)
    codigo_departamento = models.CharField(max_length=256, null=True)
    nombre_departamento = models.CharField(max_length=256, null=True)
    codigo_distrito = models.CharField(max_length=256, null=True)
    nombre_distrito = models.CharField(max_length=200, null=True)
    numero_prioridad = models.IntegerField(null=True)
    codigo_establecimiento = models.CharField(max_length=256, null=True)
    codigo_institucion = models.CharField(max_length=256, null=True)
    nombre_institucion = models.CharField(max_length=200, null=True)
    codigo_zona = models.CharField(max_length=256, null=True)
    nombre_zona = models.CharField(max_length=256, null=True)
    nivel_educativo_beneficiado = models.CharField(max_length=256, null=True)
    abastecimiento_agua = models.CharField(max_length=256, null=True)
    servicio_sanitario_actual = models.CharField(max_length=256, null=True)
    cuenta_espacio_para_construccion = models.CharField(max_length=256, null=True)
    tipo_requerimiento_infraestructura = models.CharField(max_length=200, null=True)
    cantidad_requerida = models.CharField(max_length=256, null=True)
    numero_beneficiados = models.CharField(max_length=256, null=True)
    justificacion = models.CharField(max_length=900, null=True)
    uri_establecimiento = models.CharField(max_length=256, null=True)
    uri_institucion = models.CharField(max_length=256, null=True)


class Mobiliario(models.Model):
    periodo = models.CharField(max_length=50, null=True)
    codigo_departamento = models.CharField(max_length=256, null=True)
    nombre_departamento = models.CharField(max_length=256, null=True)
    codigo_distrito = models.CharField(max_length=256, null=True)
    nombre_distrito = models.CharField(max_length=200, null=True)
    numero_prioridad = models.IntegerField(null=True)
    codigo_establecimiento = models.CharField(max_length=256, null=True)
    codigo_institucion = models.CharField(max_length=256, null=True)
    nombre_institucion = models.CharField(max_length=200, null=True)
    codigo_zona = models.CharField(max_length=256, null=True)
    nombre_zona = models.CharField(max_length=256, null=True)
    nivel_educativo_beneficiado = models.CharField(max_length=256, null=True)
    nombre_mobiliario = models.CharField(max_length=256, null=True)
    cantidad_requerida = models.CharField(max_length=256, null=True)
    numero_beneficiados = models.CharField(max_length=256, null=True)
    justificacion = models.CharField(max_length=1200, null=True)
    # No se encuentra en el csv
    # uri_establecimiento = models.CharField(max_length=256, null=True)
    # uri_institucion = models.CharField(max_length=256, null=True)


# Servicios Básicos de los establecimientos según fonacide
class ServicioBasico(models.Model):
    periodo = models.CharField(max_length=50, null=True)
    codigo_departamento = models.CharField(max_length=256, null=True)
    nombre_departamento = models.CharField(max_length=256, null=True)
    codigo_distrito = models.CharField(max_length=256, null=True)
    nombre_distrito = models.CharField(max_length=200, null=True)
    codigo_establecimiento = models.CharField(max_length=200, null=True)
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

    class Meta:
        verbose_name_plural = "serviciosbasicos"