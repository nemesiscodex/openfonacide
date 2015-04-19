# coding: utf-8
from django.core.urlresolvers import reverse
from django.db import connection
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View, TemplateView
from django.http import HttpResponse, Http404
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, filters
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework import permissions

from openfonacide.utils import dictfetch, escapelike
from openfonacide.serializers import *
from openfonacide import jsonh as JSONH


"""
ViewSets for API
"""


class PaginadorEstandard(pagination.LimitOffsetPagination):
    default_limit = 100


class OpenFonacideViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = PaginadorEstandard
    filter_backends = (filters.DjangoFilterBackend,)


class EstablecimientoViewSet(OpenFonacideViewSet):
    """
    Este `Endpoint` muestra los establecimientos escolares del MEC
    y permite filtrar los resultados por los campos
    *codigo_establecimiento*, *anio*, y *uri*

    Nota: el parámetro *anio* se refiere al año se utilizó este nombre
    para evitar problemas de codificación

    """
    serializer_class = EstablecimientoSerializer
    queryset = Establecimiento.objects.all()
    filter_fields = ('codigo_establecimiento', 'anio', 'uri', 'nombre_departamento', 'nombre_distrito')
    lookup_field = 'codigo_establecimiento'


class InstitucionViewSet(OpenFonacideViewSet):
    serializer_class = InstitucionSerializer
    queryset = Institucion.objects.all()
    filter_fields = (
        'codigo_institucion', 'codigo_establecimiento', 'periodo', 'uri_institucion', 'nombre_departamento',
        'nombre_distrito'
    )
    lookup_field = 'codigo_institucion'


class EspacioViewSet(OpenFonacideViewSet):
    serializer_class = EspacioSerializer
    queryset = Espacio.objects.all()
    filter_fields = (
        'periodo', 'codigo_establecimiento', 'codigo_institucion', 'nombre_espacio',
        'tipo_requerimiento_infraestructura'
    )
    lookup_field = 'codigo_establecimiento'


class SanitarioViewSet(OpenFonacideViewSet):
    serializer_class = SanitarioSerializer
    queryset = Sanitario.objects.all()
    filter_fields = ('periodo', 'codigo_establecimiento', 'codigo_institucion', 'tipo_requerimiento_infraestructura')
    lookup_field = 'codigo_establecimiento'


class MobiliarioViewSet(OpenFonacideViewSet):
    serializer_class = MobiliarioSerializer
    queryset = Mobiliario.objects.all()
    filter_fields = ('periodo', 'codigo_establecimiento', 'codigo_institucion')
    lookup_field = 'codigo_establecimiento'


class ServicioBasicoViewSet(OpenFonacideViewSet):
    serializer_class = ServicioBasicoSerializer
    queryset = ServicioBasico.objects.all()
    filter_fields = ('periodo', 'codigo_establecimiento')
    lookup_field = 'codigo_establecimiento'


class DummyPrioridad(object):
    espacio = None
    mobiliario = None
    sanitario = None
    servicio = None


class PrioridadAPIViewDetail(viewsets.views.APIView):
    """
    Vista para listar las prioridades, y servicios de un establecimiento
    en especifico, dado un codigo de establecimiento
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, codigo_establecimiento):
        prioridad = DummyPrioridad()
        not_found = 0
        try:
            prioridad.espacio = Espacio.objects.get(codigo_establecimiento=codigo_establecimiento)
        except Espacio.DoesNotExist:
            not_found += 1
        try:
            prioridad.mobiliario = Mobiliario.objects.get(codigo_establecimiento=codigo_establecimiento)
        except Mobiliario.DoesNotExist:
            not_found += 1
        try:
            prioridad.sanitario = Sanitario.objects.get(codigo_establecimiento=codigo_establecimiento)
        except Sanitario.DoesNotExist:
            not_found += 1
        try:
            prioridad.servicio = ServicioBasico.objects.get(codigo_establecimiento=codigo_establecimiento)
        except ServicioBasico.DoesNotExist:
            not_found += 1

        if not_found == 4:
            return Http404

        return prioridad

    def get(self, request, codigo_establecimiento, format=None):
        prioridad = self.get_object(codigo_establecimiento)
        serializer = PrioridadSerializer(prioridad)
        if format == "jsonh":
            return Response(JSONH.pack(serializer.data))
        return Response(serializer.data)


class PrioridadAPIView(viewsets.views.APIView):
    """
    Vista para listar todas las prioridades, espacios (aulas, otros)
    mobiliarios, sanitarios. Y ademas los serivicios basicos
    """
    permission_classes = (permissions.IsAuthenticated,)
    # queryset = DummyPrioridad()

    def get_queryset(self):
        queryset = DummyPrioridad()
        queryset.espacio = Espacio.objects.all()
        queryset.mobiliario = Mobiliario.objects.all()
        queryset.sanitario = Sanitario.objects.all()
        queryset.servicio = ServicioBasico.objects.all()
        return queryset

    def get(self, request, format=None):
        """
        Retorna la lista de todas las prioridades y servicios
        """
        prioridad_serializada = PrioridadSerializer(self.get_queryset())

        if format == "json":
            return JSONResponse(prioridad_serializada.data)

        if format == "jsonh":
            return JSONResponse(JSONH.pack(prioridad_serializada.data))

        return Response(prioridad_serializada.data)


class PartialGroupView(TemplateView):
    """
    Utilizada para los templates de AngularJS
    """

    def get_context_data(self, **kwargs):
        context = super(PartialGroupView, self).get_context_data(**kwargs)
        # update the context
        return context


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class Index(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('index-nuevo.html', context_instance=RequestContext(request))


# Deprecated
# class ListaInstitucionesController(View):
# def get(self, request, *args, **kwargs):
# cantidad = request.GET.get('rows')
# pagina = request.GET.get('page')
# lista = Institucion.objects.all()
# if cantidad is not None:
# paginator = Paginator(lista, cantidad)
# else:
# paginator = Paginator(lista, 10)
# total = len(lista)
# if pagina is None:
# pagina = 1
#         try:
#             instituciones = paginator.page(pagina)
#         except PageNotAnInteger:
#             instituciones = paginator.page(1)
#         except EmptyPage:
#             instituciones = paginator.page(paginator.num_pages)
#         lista_instituciones = ListaInstitucionesSerializer(instituciones, many=True)
#         # result = lista_instituciones.data
#         result = {'total': str(paginator.num_pages), 'page': pagina, 'records': str(total),
#                   'rows': lista_instituciones.data}
#         return JSONResponse(result)


class EstablecimientoController(View):
    def get(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        short = request.GET.get('short')
        query = request.GET.get('q')
        anio = request.GET.get('anio')
        if not anio:
            anio = '2014'
        if short is not None:
            if codigo_establecimiento:
                establecimiento = EstablecimientoSerializerShort(
                    Establecimiento.objects.get(codigo_establecimiento=codigo_establecimiento, anio=anio))
            else:
                if query is not None:
                    establecimiento = EstablecimientoSerializerShort(
                        Establecimiento.objects.filter(nombre__icontains=query, anio=anio) |
                        Establecimiento.objects.filter(direccion__icontains=query, anio=anio), many=True)
                    establecimiento = {"results": establecimiento.data}
                    return JSONResponse(establecimiento)
                else:
                    establecimiento = EstablecimientoSerializerShort(Establecimiento.objects.filter(anio=anio),
                                                                     many=True)
                    return JSONResponse(JSONH.pack(establecimiento.data))
        else:
            if codigo_establecimiento:
                establecimiento = EstablecimientoSerializer(
                    Establecimiento.objects.get(codigo_establecimiento=codigo_establecimiento, anio=anio))
            else:
                establecimiento = EstablecimientoSerializer(Establecimiento.objects.filter(anio=anio), many=True)
        return JSONResponse(establecimiento.data)


class InstitucionController(View):
    def get(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        query = request.GET.get('q')
        periodo = request.GET.get('periodo')
        cantidad = request.GET.get('cantidad')
        if not periodo:
            periodo = '2014'
        if codigo_establecimiento:
            institucion = InstitucionSerializer(
                Institucion.objects.filter(codigo_establecimiento=codigo_establecimiento, periodo=periodo), many=True)
        else:
            if query is not None:
                base_query = 'SELECT * FROM openfonacide_institucion inst ' \
                             'JOIN openfonacide_establecimiento est on ' \
                             '(est.anio=inst.periodo AND est.codigo_establecimiento=inst.codigo_establecimiento)'
                cursor = connection.cursor()
                cursor.execute(
                    base_query +
                    " WHERE inst.codigo_institucion like '%%" + escapelike(query.upper()) + "%%' AND inst.periodo=%s",
                    [periodo]
                )
                institucion0 = dictfetch(cursor, cantidad)
                cursor.execute(
                    base_query +
                    " WHERE inst.nombre_institucion like '%%" + escapelike(query.upper()) + "%%' AND inst.periodo=%s",
                    [periodo]
                )
                institucion1 = dictfetch(cursor, cantidad)
                cursor.execute(
                    base_query +
                    " WHERE est.direccion like '%%" + escapelike(query.upper()) + "%%' AND inst.periodo=%s",
                    [periodo]
                )
                institucion2 = dictfetch(cursor, cantidad)
                cursor.execute(
                    base_query +
                    " WHERE inst.nombre_distrito like '%%" + escapelike(query.upper()) + "%%' AND inst.periodo=%s",
                    [periodo]
                )
                institucion3 = dictfetch(cursor, cantidad)
                cursor.execute(
                    base_query +
                    " WHERE inst.nombre_barrio_localidad like '%%" + escapelike(
                        query.upper()) + "%%' AND inst.periodo=%s",
                    [periodo]
                )
                institucion4 = dictfetch(cursor, cantidad)
                print institucion2
                instituciones = {
                    "results": {
                        "category0": {
                            "name": "Codigo de Instituci&oacute;n",
                            "results": institucion0
                        },
                        "category1": {
                            "name": "Nombre",
                            "results": institucion1
                        },
                        "category2": {
                            "name": "Direccion",
                            "results": institucion2
                        },
                        "category3": {
                            "name": "Distrito",
                            "results": institucion3
                        },
                        "category4": {
                            "name": "Barrio/Localidad",
                            "results": institucion4
                        },
                        "query": query,
                        "periodo": periodo,
                        "base_url": reverse('index')
                    }
                }
                return JSONResponse(instituciones)
            else:
                institucion = InstitucionSerializer(Institucion.objects.all(), many=True)
        return JSONResponse(institucion.data)


class PrioridadController(View):
    def get(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        result = {
            "aulas": get_Pr(codigo_establecimiento, Espacio, EspacioSerializer).data,
            "sanitarios": get_Pr(codigo_establecimiento, Sanitario,
                                 SanitarioSerializer).data,
            "mobiliarios": get_Pr(codigo_establecimiento, Mobiliario,
                                  MobiliarioSerializer).data,
            "estados": get_Pr(codigo_establecimiento, ServicioBasico,
                              ServicioBasicoSerializer).data,


        }
        return JSONResponse(result)


# class TotalPrioridadController(View):
# def get(self, request, *args, **kwargs):
#
#         result = {
#             "establecimietos": get_fonacide().data,
#
#
#
#
#         }
#         return JSONResponse(result)


class ComentariosController(View):
    pass

    # Not yet Implemented
    # def get(self, request, *args, **kwargs):
    #     codigo_establecimiento = kwargs.get('codigo_establecimiento')
    #     comentarios = Comentarios.objects.filter(codigo_establecimiento=codigo_establecimiento).order_by('fecha')
    #     return JSONResponse(ComentariosSerializer(comentarios, many=True).data)
    #
    # def post(self, request, *args, **kwargs):
    #     codigo_establecimiento = kwargs.get('codigo_establecimiento')
    #
    #     captcha = json.loads(request.POST.get('captcha'))
    #
    #     # captcha_result = urllib2.urlopen("https://www.google.com/recaptcha/api/siteverify",
    #     #                                  data=urllib.urlencode({
    #     #                                      "secret": "secret",
    #     #                                      "response": captcha
    #     #                                  })).read()
    #
    #     # analize captcha result
    #
    #     comentario = Comentarios()
    #     comentario.codigo_establecimiento_id = codigo_establecimiento
    #     comentario.autor = request.POST.get('autor')
    #     comentario.email = request.POST.get('email')
    #     comentario.texto = request.POST.get('texto')
    #     comentario.fecha = datetime.datetime.now()
    #     comentario.save()
    #     return JSONResponse({"success": True});
