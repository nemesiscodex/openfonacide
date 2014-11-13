from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer
from mecmapi.models import Institucion
from mecmapi.utils import conversion


class InstitucionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = ('anio', 'codigo_establecimiento', 'codigo_departamento', 'nombre_departamento', 'codigo_distrito',
                  'nombre_distrito', 'codigo_zona', 'nombre_zona', 'codigo_barrio_localidad', 'nombre_barrio_localidad',
                  'direccion', 'coordenadas_y', 'coordenadas_x', 'latitud', 'longitud', 'anho_cod_geo', 'programa',
                  'proyecto_111', 'proyecto_822', 'uri')


class InstitucionesSerializerShort(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_field_id_short_name')
    lat = serializers.SerializerMethodField('get_field_lat_short_name')
    lon = serializers.SerializerMethodField('get_field_lon_short_name')
    class Meta:
        model = Institucion
        fields = ('id', 'lat', 'lon')

    def get_field_id_short_name(self, obj):
        return obj.codigo_establecimiento

    def get_field_lat_short_name(self, obj):
        if obj.latitud:
            return conversion(obj.latitud)
        return "0"

    def get_field_lon_short_name(self, obj):
        if obj.longitud:
            return conversion(obj.longitud)
        return "0"