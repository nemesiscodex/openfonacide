"""
Open data mec map api models
"""

from django.db import models


class Institucion(models.Model):
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
    programa = models.CharField(max_length=256)
    proyecto_111 = models.CharField(max_length=256)
    proyecto_822 = models.CharField(max_length=256)
    uri = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256, default='<Sin nombre>')
    fonacide = models.CharField(max_length=5, null=True)



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
    codigo_establecimiento = models.ForeignKey('Institucion')
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


# Prioridades

class ConstruccionAulas(models.Model):
    prioridad = models.IntegerField(null=True)
    cod_local = models.CharField(max_length=256, null=True)
    cod_institucion = models.CharField(max_length=256, null=True)
    nombre_institucion = models.CharField(max_length=200)
    nro_esc = models.CharField(max_length=256, null=True)
    distrito = models.CharField(max_length=200, null=True)
    localidad_barrio = models.CharField(max_length=256, null=True)
    zona = models.CharField(max_length=256, null=True)
    nombre_asentamiento = models.CharField(max_length=256, null=True)
    region_supervision = models.CharField(max_length=256, null=True)
    nro_beneficiados = models.CharField(max_length=256, null=True)
    nivel_educativo_beneficiado = models.CharField(max_length=256, null=True)
    espacio_destinado = models.CharField(max_length=200, null=True)
    cantidad_espacios_nuevos = models.CharField(max_length=256, null=True)
    abastecimiento_agua = models.CharField(max_length=256, null=True)
    corriente_electrica = models.CharField(max_length=256, null=True)
    titulo_propiedad = models.CharField(max_length=256, null=True)
    cuenta_con_espacio_construccion = models.CharField(max_length=256, null=True)
    justificacion = models.CharField(max_length=500, null=True)
    departamento = models.CharField(max_length=256, null=True)
    cod_departamento = models.CharField(max_length=256, null=True)

class ConstruccionSanitario(models.Model):
    prioridad = models.IntegerField(null=True)
    cod_local = models.CharField(max_length=256, null=True)
    cod_institucion = models.CharField(max_length=256, null=True)
    nombre_institucion = models.CharField(max_length=200, null=True)
    nro_esc = models.CharField(max_length=256, null=True)
    distrito = models.CharField(max_length=200, null=True)
    localidad_barrio = models.CharField(max_length=256, null=True)
    zona = models.CharField(max_length=256, null=True)
    nombre_asentamiento = models.CharField(max_length=256, null=True)
    region_supervision = models.CharField(max_length=256, null=True)
    nro_beneficiados = models.CharField(max_length=256, null=True)
    nivel_educativo_beneficiado = models.CharField(max_length=256, null=True)
    cant_sanitarios_construccion = models.CharField(max_length=256, null=True)
    abastecimiento_agua = models.CharField(max_length=256, null=True)
    corriente_electrica = models.CharField(max_length=256, null=True)
    titulo_propiedad = models.CharField(max_length=256, null=True)
    cuenta_con_espacio = models.CharField(max_length=256, null=True)
    justificacion = models.CharField(max_length=500, null=True)
    departamento = models.CharField(max_length=256, null=True)
    cod_departamento = models.CharField(max_length=256, null=True)

class ReparacionAulas(models.Model):
    prioridad = models.IntegerField(null=True)
    cod_local = models.CharField(max_length=256, null=True)
    cod_institucion = models.CharField(max_length=256, null=True)
    nombre_institucion = models.CharField(max_length=200, null=True)
    nro_esc = models.CharField(max_length=256, null=True)
    distrito = models.CharField(max_length=200, null=True)
    localidad_barrio = models.CharField(max_length=256, null=True)
    zona = models.CharField(max_length=256, null=True)
    nombre_asentamiento = models.CharField(max_length=256, null=True)
    region_supervision = models.CharField(max_length=256, null=True)
    nro_beneficiados = models.CharField(max_length=256, null=True)
    nivel_educativo_beneficiado = models.CharField(max_length=256, null=True)
    espacio_destinado_a = models.CharField(max_length=256, null=True)
    cant_espacios_necesitan_reparacion = models.CharField(max_length=256, null=True)
    cant_espacios_construidos_adecuacion = models.CharField(max_length=256, null=True)
    justificacion = models.CharField(max_length=500, null=True)
    departamento = models.CharField(max_length=256, null=True)
    cod_departamento = models.CharField(max_length=256, null=True)


class ReparacionSanitario(models.Model):
    prioridad = models.IntegerField(null=True)
    cod_local = models.CharField(max_length=256, null=True)
    cod_institucion = models.CharField(max_length=256, null=True)
    nombre_institucion = models.CharField(max_length=200, null=True)
    nro_esc = models.CharField(max_length=256, null=True)
    distrito = models.CharField(max_length=200, null=True)
    localidad_barrio = models.CharField(max_length=256, null=True)
    zona = models.CharField(max_length=256, null=True)
    nombre_asentamiento = models.CharField(max_length=256, null=True)
    region_supervision = models.CharField(max_length=256, null=True)
    nro_beneficiados = models.CharField(max_length=256, null=True)
    nivel_educativo_beneficiado = models.CharField(max_length=256, null=True)
    cantidad_sanitarios_construidos_reparacion = models.CharField(max_length=256, null=True)
    cantidad_sanitarios_construidos_adecuacion = models.CharField(max_length=256, null=True)
    justificacion = models.CharField(max_length=500, null=True)
    departamento = models.CharField(max_length=256, null=True)
    cod_departamento = models.CharField(max_length=256, null=True)

class Adjudicacion(models.Model):
    codigo_adjudicacion = models.CharField(max_length=256)
    codigo_establecimiento = models.ForeignKey('Institucion')
    llamado = models.CharField(max_length=256)
    monto = models.IntegerField(null=False)
    entidad = models.CharField(max_length=256)
    estado = models.CharField(max_length=256)
    anio = models.IntegerField(null=False)


class Comentarios(models.Model):
    codigo_establecimiento = models.ForeignKey('Institucion')
    texto = models.CharField(max_length=1024, null=False)
    autor = models.CharField(max_length=256, null=False)
    fecha = models.DateField(null=False)
    email = models.CharField(max_length=256, null=False)



#Prioridades 2.0###############################################################################

           


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
    numero_beneficiados  = models.CharField(max_length=256, null=True)
    justificacion = models.CharField(max_length=900, null=True)
    uri_establecimiento  = models.CharField(max_length=256, null=True)
    uri_institucion  = models.CharField(max_length=256, null=True)


    




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
    numero_beneficiados  = models.CharField(max_length=256, null=True)
    justificacion = models.CharField(max_length=900, null=True)    
   
    uri_establecimiento  = models.CharField(max_length=256, null=True)
    uri_institucion  = models.CharField(max_length=256, null=True)


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
    numero_beneficiados  = models.CharField(max_length=256, null=True)
    justificacion = models.CharField(max_length=1200, null=True)       
    uri_establecimiento  = models.CharField(max_length=256, null=True)
    uri_institucion  = models.CharField(max_length=256, null=True)






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
    servicio_sanitario_actual  = models.CharField(max_length=256, null=True)
    titulo_de_propiedad  = models.CharField(max_length=256, null=True)
    cuenta_plano = models.CharField(max_length=256, null=True)
    prevencion_incendio = models.CharField(max_length=256, null=True)
    uri_establecimiento = models.CharField(max_length=256, null=True)

    