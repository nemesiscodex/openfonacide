from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from openfonacide.models import *

#
# @admin.register(ReparacionSanitario)
# class ReparacionSanitarioAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(ReparacionAulas)
# class ReparacionAulasAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(ConstruccionSanitario)
# class ConstruccionSanitarioAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(ConstruccionAulas)
# class ConstruccionAulasAdmin(admin.ModelAdmin):
#     pass


class SanitariosResource(resources.ModelResource):

    class Meta:
        model = Sanitarios
        # exclude = ('id',)


@admin.register(Sanitarios)
class SanitariosAdmin(ImportExportModelAdmin):
    resource_class = SanitariosResource
    pass


class EspaciosResource(resources.ModelResource):

    class Meta:
        model = Espacios
        # exclude = ('id',)


@admin.register(Espacios)
class EspaciosAdmin(ImportExportModelAdmin):
    resource_class = EspaciosResource
    pass




class MobiliariosResource(resources.ModelResource):

    class Meta:
        model = Mobiliarios
        # exclude = ('id',)


@admin.register(Mobiliarios)
class MobiliariosAdmin(ImportExportModelAdmin):
    resource_class = MobiliariosResource
    pass




class EstadosResource(resources.ModelResource):

    class Meta:
        model = EstadosLocales
        # exclude = ('id',)


@admin.register(EstadosLocales)
class EstadosAdmin(ImportExportModelAdmin):
    resource_class = EstadosResource
    pass
