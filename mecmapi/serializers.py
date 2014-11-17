from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer
from mecmapi.models import Institucion, InstitucionData
from mecmapi.utils import conversion


class EstablecimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = ('anio', 'codigo_establecimiento', 'codigo_departamento', 'nombre_departamento', 'codigo_distrito',
                  'nombre_distrito', 'codigo_zona', 'nombre_zona', 'codigo_barrio_localidad', 'nombre_barrio_localidad',
                  'direccion', 'coordenadas_y', 'coordenadas_x', 'latitud', 'longitud', 'anho_cod_geo', 'programa',
                  'proyecto_111', 'proyecto_822', 'uri')


class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitucionData
        fields = ('anio', 'codigo_departamento', 'nombre_departamento', 'codigo_distrito', 'nombre_distrito',
                  'codigo_barrio_localidad', 'nombre_barrio_localidad', 'codigo_zona', 'nombre_zona',
                  'codigo_establecimiento', 'codigo_institucion', 'nombre_institucion', 'sector_o_tipo_gestion',
                  'codigo_region_administrativa', 'nombre_region_administrativa', 'nombre_supervisor',
                  'niveles_modalidades', 'codigo_tipo_organizacion', 'nombre_tipo_organizacion',
                  'participacion_comunitaria', 'direccion', 'nro_telefono', 'tiene_internet', 'paginaweb',
                  'correo_electronico')


class EstablecimientoSerializerShort(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_field_id_short_name')
    lat = serializers.SerializerMethodField('get_field_lat_short_name')
    lon = serializers.SerializerMethodField('get_field_lon_short_name')
    name = serializers.SerializerMethodField('get_field_name_short_name')
    dir = serializers.SerializerMethodField('get_field_dir_short_name')
    class Meta:
        model = Institucion
        fields = ('id', 'lat', 'lon','name','dir')

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
            return obj.nombre.replace('{', '').replace('}', '').replace('","', '\n').replace('"','')
        return "<Sin nombre>"