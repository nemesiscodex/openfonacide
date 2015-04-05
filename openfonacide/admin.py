from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from openfonacide.models import *

class EstablecimientoResource(resources.ModelResource):

    class Meta:
        model = Establecimiento
        # exclude = ('id',)


@admin.register(Establecimiento)
class EstablecimientoAdmin(ImportExportModelAdmin):
    resource_class = EstablecimientoResource
    pass


class InstitucionResource(resources.ModelResource):

    class Meta:
        model = Institucion
        # exclude = ('id',)


@admin.register(Institucion)
class InstitucionAdmin(ImportExportModelAdmin):
    resource_class = InstitucionResource
    pass


class SanitariosResource(resources.ModelResource):

    class Meta:
        model = Sanitario
        # exclude = ('id',)


@admin.register(Sanitario)
class SanitariosAdmin(ImportExportModelAdmin):
    resource_class = SanitariosResource
    pass


class EspaciosResource(resources.ModelResource):
    class Meta:
        model = Espacio
        # exclude = ('id',)


@admin.register(Espacio)
class EspaciosAdmin(ImportExportModelAdmin):
    resource_class = EspaciosResource
    pass




class MobiliariosResource(resources.ModelResource):

    class Meta:
        model = Mobiliario
        # exclude = ('id',)


@admin.register(Mobiliario)
class MobiliariosAdmin(ImportExportModelAdmin):
    resource_class = MobiliariosResource
    pass




class EstadosResource(resources.ModelResource):

    class Meta:
        model = ServicioBasico
        # exclude = ('id',)


@admin.register(ServicioBasico)
class EstadosAdmin(ImportExportModelAdmin):
    resource_class = EstadosResource
    pass
