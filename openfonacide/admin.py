from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from openfonacide.models import *

@admin.register(NotificacionesReportes)
class NotificacionesReportesAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Notificaciones", {
            'fields': ('email',),
            'description': "A este correo se enviar&aacute;n notificaciones por cada <strong>Reporte</strong> de la "
                           "ciudadan&iacute;a sobre las prioridades."
        }),
    )

# AUN NO IMPLEMENTADO
# @admin.register(NotificacionesCambioDeEstado)
# class NotificacionesCambioDeEstadoAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ("Notificaciones", {
#             'fields': ('email',),
#             'description': "A este correo se enviar&aacute;n notificaciones por cada <strong>Cambio de Estado</strong> "
#                            "en las obras."
#         }),
#     )
#
#
# @admin.register(NotificacionesVerificacion)
# class NotificacionesVerificacionAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ("Notificaciones", {
#             'fields': ('email',),
#             'description': "A este correo se enviar&aacute;n notificaciones por cada "
#                            "<strong>Verificaci&oacute;n</strong> hecha sobre el Estado de una obra."
#         }),
#     )

class ImportacionResource(resources.ModelResource):
    class Meta:
        model = Importacion

@admin.register(Importacion)
class ImportacionAdmin(ImportExportModelAdmin):
    resource_class = ImportacionResource
    pass

class AdjudicacionResource(resources.ModelResource):
    class Meta:
        model = Adjudicacion


@admin.register(Adjudicacion)
class AdjudicacionAdmin(ImportExportModelAdmin):
    resource_class = AdjudicacionResource
    pass


class PlanificacionResource(resources.ModelResource):
    class Meta:
        model = Planificacion
        # exclude = ('id',)


@admin.register(Planificacion)
class PlanificacionAdmin(ImportExportModelAdmin):
    resource_class = PlanificacionResource
    pass


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
