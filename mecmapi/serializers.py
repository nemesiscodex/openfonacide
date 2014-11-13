from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer
from mecmapi.models import Institucion


class InstitucionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = ('anio', 'codigo_establecimiento', 'codigo_departamento', 'nombre_departamento', 'codigo_distrito',
                  'nombre_distrito', 'codigo_zona', 'nombre_zona', 'codigo_barrio_localidad', 'nombre_barrio_localidad',
                  'direccion', 'coordenadas_y', 'coordenadas_x', 'latitud', 'longitud', 'anho_cod_geo', 'programa',
                  'proyecto_111', 'proyecto_822', 'uri',)