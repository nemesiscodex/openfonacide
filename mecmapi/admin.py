from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from mecmapi.models import *

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

class ReparacionSanitarioResource(resources.ModelResource):

    class Meta:
        model = ReparacionSanitario
        # exclude = ('id',)

@admin.register(ReparacionSanitario)
class ReparacionSanitarioAdmin(ImportExportModelAdmin):
    resource_class = ReparacionSanitarioResource
    pass


class ReparacionAulasResource(resources.ModelResource):

    class Meta:
        model = ReparacionAulas
        # exclude = ('id',)

@admin.register(ReparacionAulas)
class ReparacionAulasAdmin(ImportExportModelAdmin):
    resource_class = ReparacionAulasResource
    pass


class ConstruccionAulasResource(resources.ModelResource):

    class Meta:
        model = ConstruccionAulas
        # exclude = ('id',)

@admin.register(ConstruccionAulas)
class ConstruccionAulasAdmin(ImportExportModelAdmin):
    resource_class = ConstruccionAulasResource
    pass

class ConstruccionSanitarioResource(resources.ModelResource):

    class Meta:
        model = ConstruccionSanitario
        # exclude = ('id',)

@admin.register(ConstruccionSanitario)
class ConstruccionSanitarioAdmin(ImportExportModelAdmin):
    resource_class = ConstruccionSanitarioResource
    pass


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