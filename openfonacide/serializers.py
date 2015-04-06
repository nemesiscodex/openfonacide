from rest_framework import serializers

from openfonacide.models import *
from openfonacide.utils import conversion


class EstablecimientoSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('get_field_title')
    description = serializers.SerializerMethodField('get_field_description')
    longitud = serializers.SerializerMethodField('get_field_lon')
    latitud = serializers.SerializerMethodField('get_field_lat')

    class Meta:
        model = Establecimiento
        fields = (
            'anio',
            'codigo_establecimiento',
            'codigo_departamento',
            'nombre_departamento',
            'codigo_distrito',
            'nombre_distrito',
            'codigo_zona',
            'nombre_zona',
            'codigo_barrio_localidad',
            'nombre_barrio_localidad',
            'direccion',
            'coordenadas_y',
            'coordenadas_x',
            'latitud',
            'longitud',
            'anho_cod_geo',
            'uri',
            # Nombre corresponde a la concatenacion de los nombres de instituciones
            # dentro de el establecimiento
            'nombre',
            # Fonacide es una variable calculada, correspondiente a si esta en una lista de prioridades
            'fonacide',
            'title',
            'description'
        )

    def get_field_title(self, obj):
        return obj.nombre.replace('{', '').replace('}', '')

    def get_field_description(self, obj):
        return obj.direccion

    def get_field_lat(self, obj):
        if obj.latitud:
            return "%2.5f" % conversion(obj.latitud)
        return "0"

    def get_field_lon(self, obj):
        if obj.longitud:
            return "%2.5f" % conversion(obj.longitud)
        return "0"


class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = (
            'periodo',
            'codigo_departamento',
            'nombre_departamento',
            'codigo_distrito',
            'nombre_distrito',
            'codigo_barrio_localidad',
            'nombre_barrio_localidad',
            'codigo_zona',
            'nombre_zona',
            'codigo_establecimiento',
            'codigo_institucion',
            'nombre_institucion',
            'anho_cod_geo',
            'uri_establecimiento',
            'uri_institucion',
        )


# Deprecated
# class ListaInstitucionesSerializer(serializers.ModelSerializer):
# class Meta:
#         model = Institucion
#         fields = ('codigo_establecimiento',
#                   'codigo_institucion',
#                   'nombre_institucion',
#                   'nombre_departamento',
#                   'nombre_distrito',
#                   'nombre_barrio_localidad',
#                   'nombre_region_administrativa',
#                   'nombre_supervisor',
#                   'niveles_modalidades',
#                   'direccion',
#                   'nro_telefono')


class EstablecimientoSerializerShort(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_field_id_short_name')
    lat = serializers.SerializerMethodField('get_field_lat_short_name')
    lon = serializers.SerializerMethodField('get_field_lon_short_name')
    name = serializers.SerializerMethodField('get_field_name_short_name')
    dir = serializers.SerializerMethodField('get_field_dir_short_name')
    f = serializers.SerializerMethodField('get_field_f_short_name')

    class Meta:
        model = Establecimiento
        fields = ('id',
                  'lat',
                  'lon',
                  'name',
                  'dir',
                  'f')

    def get_field_id_short_name(self, obj):
        return obj.codigo_establecimiento

    def get_field_dir_short_name(self, obj):
        return obj.direccion

    def get_field_lat_short_name(self, obj):
        if obj.latitud:
            return "%2.5f" % conversion(obj.latitud)
        return "0"

    def get_field_lon_short_name(self, obj):
        if obj.longitud:
            return "%2.5f" % conversion(obj.longitud)
        return "0"

    def get_field_name_short_name(self, obj):
        if obj.codigo_establecimiento:
            return obj.nombre.replace('{', '').replace('}', '').replace('","', '\n').replace('"', '')
        return "<Sin nombre>"

    def get_field_f_short_name(self, obj):
        if obj.fonacide is None:
            return 'f'
        else:
            return 't'


class PrioridadesSerializer(serializers.Serializer):
    construccion_aulas = serializers.SerializerMethodField('get_construccion_aulas')

    class Meta:
        fields = ('construccion_aulas',)


def get_P(establecimiento, prioridadClass, serializerClass):
    if not establecimiento:
        return serializerClass(prioridadClass.objects.all(), many=True)
    instituciones = Institucion.objects.filter(codigo_establecimiento=establecimiento)
    data = prioridadClass.objects.filter(codigo_local=establecimiento)
    for institucion in instituciones:
        data = data | prioridadClass.objects.filter(codigo_institucion=institucion.codigo_institucion)
    return serializerClass(data, many=True)


def get_Pr(establecimiento, prioridadClass, serializerClass):
    if not establecimiento:
        return serializerClass(prioridadClass.objects.all(), many=True)
    instituciones = Institucion.objects.filter(codigo_establecimiento=establecimiento)
    data = prioridadClass.objects.filter(codigo_establecimiento=establecimiento)
    for institucion in instituciones:
        data = data | prioridadClass.objects.filter(codigo_establecimiento=institucion.codigo_institucion)
    return serializerClass(data, many=True)


class EspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacio
        fields = (
            "periodo",
            "codigo_departamento",
            "nombre_departamento",
            "codigo_distrito",
            "nombre_distrito",
            "numero_prioridad",
            "codigo_establecimiento",
            "codigo_institucion",
            "nombre_institucion",
            "codigo_zona",
            "nombre_zona",
            "nivel_educativo_beneficiado",
            "cuenta_espacio_para_construccion",
            "nombre_espacio",
            "tipo_requerimiento_infraestructura",
            "cantidad_requerida",
            "numero_beneficiados",
            "justificacion",
            "uri_establecimiento",
            "uri_institucion"
        )


class SanitarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sanitario
        fields = (
            "periodo",
            "codigo_departamento",
            "nombre_departamento",
            "codigo_distrito",
            "nombre_distrito",
            "numero_prioridad",
            "codigo_establecimiento",
            "codigo_institucion",
            "nombre_institucion",
            "codigo_zona",
            "nombre_zona",
            "nivel_educativo_beneficiado",
            "abastecimiento_agua",
            "servicio_sanitario_actual",
            "cuenta_espacio_para_construccion",
            "tipo_requerimiento_infraestructura",
            "cantidad_requerida",
            "numero_beneficiados",
            "justificacion",
            "uri_establecimiento",
            "uri_institucion"
        )


class MobiliarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobiliario
        fields = (
            "periodo",
            "codigo_departamento",
            "nombre_departamento",
            "codigo_distrito",
            "nombre_distrito",
            "numero_prioridad",
            "codigo_establecimiento",
            "codigo_institucion",
            "nombre_institucion",
            "codigo_zona",
            "nombre_zona",
            "nivel_educativo_beneficiado",
            "nombre_mobiliario",
            "cantidad_requerida",
            "numero_beneficiados",
            "justificacion",
            "uri_establecimiento",
            "uri_institucion"
        )


class ServicioBasicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioBasico
        fields = (
            "periodo",
            "codigo_departamento",
            "nombre_departamento",
            "codigo_distrito",
            "nombre_distrito",
            "codigo_establecimiento",
            "codigo_barrio_localidad",
            "nombre_barrio_localidad",
            "codigo_zona",
            "nombre_zona",
            "nombre_asentamiento_colonia",
            "suministro_energia_electrica",
            "abastecimiento_agua",
            "servicio_sanitario_actual",
            "titulo_de_propiedad",
            "cuenta_plano",
            "prevencion_incendio",
            "uri_establecimiento"
        )


class PrioridadSerializer(serializers.Serializer):

    espacio = EspacioSerializer(read_only=True, many=True)
    sanitario = SanitarioSerializer(read_only=True, many=True)
    mobiliario = MobiliarioSerializer(read_only=True, many=True)
    servicio = ServicioBasicoSerializer(read_only=True, many=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass