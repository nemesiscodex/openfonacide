# encoding: utf-8
"""
OpenFonacide Models
Modelo de datos utilizado en OpenFonacide
"""

from django.db import models


class Establecimiento(models.Model):
    """
    Modelo de datos que representa los Establecimientos
    """
    anio = models.CharField(max_length=256)
    codigo_establecimiento = models.CharField(max_length=256, db_index=True)
    codigo_departamento = models.CharField(max_length=256, db_index=True)
    nombre_departamento = models.CharField(max_length=256)
    codigo_distrito = models.CharField(max_length=256, db_index=True)
    nombre_distrito = models.CharField(max_length=256)
    codigo_zona = models.CharField(max_length=256, db_index=True)
    nombre_zona = models.CharField(max_length=256)
    codigo_barrio_localidad = models.CharField(max_length=256, db_index=True)
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
        verbose_name_plural = 'establecimientos'
        unique_together = (("anio", "codigo_establecimiento"),)


# Planificacion de Fonacide
class Planificacion(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    anio = models.CharField(max_length=50, null=True)
    id_llamado = models.CharField(max_length=200, null=True)
    nombre_licitacion = models.CharField(max_length=1024, null=True)
    convocante = models.CharField(max_length=200, null=True)
    codigo_sicp = models.CharField(max_length=50, null=True)
    categoria_id = models.CharField(max_length=50, null=True)
    categoria_codigo = models.CharField(max_length=200, null=True)
    categoria = models.CharField(max_length=200, null=True)
    tipo_procedimiento_id = models.CharField(max_length=50, null=True)
    tipo_procedimiento_codigo = models.CharField(max_length=50, null=True)
    tipo_procedimiento = models.CharField(max_length=200, null=True)
    fecha_estimada = models.CharField(max_length=50, null=True)
    fecha_publicacion = models.CharField(max_length=50, null=True)
    _moneda = models.CharField(max_length=50, null=True)
    moneda = models.CharField(max_length=50, null=True)
    _estado = models.CharField(max_length=200, null=True)
    estado = models.CharField(max_length=200, null=True)
    _objeto_licitacion = models.CharField(max_length=200, null=True)
    objeto_licitacion = models.CharField(max_length=200, null=True)
    etiquetas = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name_plural = "planificaciones"


class Adjudicacion(models.Model):
    id = models.CharField(max_length=1024, null=False, primary_key=True)
    planificacion_id = models.CharField(max_length=1024, null=False)
    convocatoria_id = models.CharField(max_length=1024, null=False)
    id_llamado = models.CharField(max_length=255, null=False)
    nombre_licitacion = models.TextField(null=True)
    convocante = models.CharField(max_length=1024, null=True)
    codigo_sicp = models.CharField(max_length=255, null=True)
    categoria_id = models.CharField(max_length=255, null=True)
    categoria_codigo = models.CharField(max_length=255, null=True)
    categoria = models.CharField(max_length=255, null=True)
    tipo_procedimiento_id = models.CharField(max_length=255, null=True)
    tipo_procedimiento_codigo = models.CharField(max_length=255, null=True)
    tipo_procedimiento = models.CharField(max_length=255, null=True)
    _estado = models.CharField(max_length=255, null=True)
    estado = models.CharField(max_length=255, null=True)
    _sistema_adjudicacion = models.CharField(max_length=255, null=True)
    sistema_adjudicacion = models.CharField(max_length=255, null=True)
    monto_total_adjudicado = models.CharField(max_length=255, null=True)
    monto_periodo = models.CharField(max_length=255, null=True)
    _moneda = models.CharField(max_length=255, null=True)
    moneda = models.CharField(max_length=255, null=True)
    fecha_publicacion = models.CharField(max_length=255, null=True)
    observaciones = models.CharField(max_length=1024, null=True)
    restricciones = models.CharField(max_length=512, null=True)
    organismo_financiador_id = models.CharField(max_length=255, null=True)
    organismo_financiador = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = "adjudicaciones"


# Datos Específicos de Instituciones Educativas
class Institucion(models.Model):
    periodo = models.CharField(max_length=256)
    codigo_departamento = models.CharField(max_length=256, db_index=True)
    nombre_departamento = models.CharField(max_length=256)
    codigo_distrito = models.CharField(max_length=256, db_index=True)
    nombre_distrito = models.CharField(max_length=256)
    codigo_barrio_localidad = models.CharField(max_length=256, db_index=True)
    nombre_barrio_localidad = models.CharField(max_length=256)
    codigo_zona = models.CharField(max_length=256, db_index=True)
    nombre_zona = models.CharField(max_length=256)
    codigo_establecimiento = models.CharField(max_length=256, db_index=True)
    codigo_institucion = models.CharField(max_length=256, db_index=True)
    nombre_institucion = models.CharField(max_length=256)
    anho_cod_geo = models.CharField(max_length=256)
    uri_establecimiento = models.CharField(max_length=256, null=True)
    uri_institucion = models.CharField(max_length=256, null=True)

    planificaciones = models.ManyToManyRel(Planificacion)
    adjudicaciones = models.ManyToManyRel(Adjudicacion)

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
# En este modelo se representan los datasets de Aulas y Otros Espacios
# por que solo difieren en el valor del campo espacio_destinado
class Espacio(models.Model):
    periodo = models.CharField(max_length=50, null=True)
    codigo_departamento = models.CharField(max_length=256, null=True, db_index=True)
    nombre_departamento = models.CharField(max_length=256, null=True)
    codigo_distrito = models.CharField(max_length=256, null=True, db_index=True)
    nombre_distrito = models.CharField(max_length=200, null=True)
    numero_prioridad = models.IntegerField(null=True, db_index=True)
    codigo_establecimiento = models.CharField(max_length=256, null=True, db_index=True)
    codigo_institucion = models.CharField(max_length=256, null=True, db_index=True)
    nombre_institucion = models.CharField(max_length=200)
    codigo_zona = models.CharField(max_length=256, null=True, db_index=True)
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
    codigo_departamento = models.CharField(max_length=256, null=True, db_index=True)
    nombre_departamento = models.CharField(max_length=256, null=True)
    codigo_distrito = models.CharField(max_length=256, null=True, db_index=True)
    nombre_distrito = models.CharField(max_length=200, null=True)
    numero_prioridad = models.IntegerField(null=True, db_index=True)
    codigo_establecimiento = models.CharField(max_length=256, null=True, db_index=True)
    codigo_institucion = models.CharField(max_length=256, null=True, db_index=True)
    nombre_institucion = models.CharField(max_length=200, null=True)
    codigo_zona = models.CharField(max_length=256, null=True, db_index=True)
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
    codigo_departamento = models.CharField(max_length=256, null=True, db_index=True)
    nombre_departamento = models.CharField(max_length=256, null=True)
    codigo_distrito = models.CharField(max_length=256, null=True, db_index=True)
    nombre_distrito = models.CharField(max_length=200, null=True)
    numero_prioridad = models.IntegerField(null=True, db_index=True)
    codigo_establecimiento = models.CharField(max_length=256, null=True, db_index=True)
    codigo_institucion = models.CharField(max_length=256, null=True, db_index=True)
    nombre_institucion = models.CharField(max_length=200, null=True)
    codigo_zona = models.CharField(max_length=256, null=True, db_index=True)
    nombre_zona = models.CharField(max_length=256, null=True)
    nivel_educativo_beneficiado = models.CharField(max_length=256, null=True)
    nombre_mobiliario = models.CharField(max_length=256, null=True)
    cantidad_requerida = models.CharField(max_length=256, null=True)
    numero_beneficiados = models.CharField(max_length=256, null=True)
    justificacion = models.CharField(max_length=1200, null=True)
    # Tener especial consideracion, puede no existir en la fuente
    uri_establecimiento = models.CharField(max_length=256, null=True)
    uri_institucion = models.CharField(max_length=256, null=True)


# Servicios Básicos de los establecimientos según fonacide
class ServicioBasico(models.Model):
    periodo = models.CharField(max_length=50, null=True)
    codigo_departamento = models.CharField(max_length=256, null=True, db_index=True)
    nombre_departamento = models.CharField(max_length=256, null=True)
    codigo_distrito = models.CharField(max_length=256, null=True, db_index=True)
    nombre_distrito = models.CharField(max_length=200, null=True)
    codigo_establecimiento = models.CharField(max_length=200, null=True, db_index=True)
    codigo_barrio_localidad = models.CharField(max_length=200, null=True, db_index=True)
    nombre_barrio_localidad = models.CharField(max_length=200, null=True)
    codigo_zona = models.CharField(max_length=256, null=True, db_index=True)
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


# Tabla Temporal que almacena los resultados del String Matcher
class Temporal(models.Model):
    """
    Este modelo representa una tabla temporal que almacena información sobre
    los posibles resultados del String Matcher aplicado.
    Esta tabla se borra cada vez que se accede a la vista del matcher y se
    carga cada vez que se Invoca la operación.
    """
    # MEC
    periodo = models.CharField(max_length=256)
    nombre_departamento = models.CharField(max_length=256)
    nombre_distrito = models.CharField(max_length=256)
    codigo_institucion = models.CharField(max_length=256)
    nombre_institucion = models.CharField(max_length=256, null=True)
    # DNCP
    id_planificacion = models.CharField(max_length=200, null=True)
    anio = models.CharField(max_length=50, null=True)
    id_llamado = models.CharField(max_length=200, null=True)
    nombre_licitacion = models.CharField(max_length=1024, null=True)
    convocante = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = "temporales"