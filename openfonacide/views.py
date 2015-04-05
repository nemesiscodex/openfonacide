import datetime
import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from rest_framework import pagination

from openfonacide.serializers import *
from openfonacide import jsonh as JSONH


"""
    ViewSets for API
"""


class PaginadorEstandard(pagination.LimitOffsetPagination):
    default_limit = 100


class OpenFonacideViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = PaginadorEstandard


class EstablecimientoViewSet(OpenFonacideViewSet):
    serializer_class = EstablecimientoSerializer
    queryset = Establecimiento.objects.all()


class InstitucionViewSet(OpenFonacideViewSet):
    serializer_class = InstitucionSerializer
    queryset = Institucion.objects.all()


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
#         cantidad = request.GET.get('rows')
#         pagina = request.GET.get('page')
#         lista = Institucion.objects.all()
#         if cantidad is not None:
#             paginator = Paginator(lista, cantidad)
#         else:
#             paginator = Paginator(lista, 10)
#         total = len(lista)
#         if pagina is None:
#             pagina = 1
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
        if short is not None:
            if codigo_establecimiento:
                establecimiento = EstablecimientoSerializerShort(
                    Establecimiento.objects.get(codigo_establecimiento=codigo_establecimiento))
            else:
                if query is not None:
                    establecimiento = EstablecimientoSerializerShort(
                        Establecimiento.objects.filter(nombre__icontains=query) |
                        Establecimiento.objects.filter(direccion__icontains=query), many=True)
                    establecimiento = {"results": establecimiento.data}
                    return JSONResponse(establecimiento)
                else:
                    establecimiento = EstablecimientoSerializerShort(Establecimiento.objects.all(), many=True)
                    return JSONResponse(JSONH.pack(establecimiento.data))
        else:
            if codigo_establecimiento:
                establecimiento = EstablecimientoSerializer(
                    Establecimiento.objects.get(codigo_establecimiento=codigo_establecimiento))
            else:
                if query is not None:
                    establecimiento1 = EstablecimientoSerializer(
                        Establecimiento.objects.filter(nombre__icontains=query)[:10],
                        many=True)
                    establecimiento2 = EstablecimientoSerializer(
                        Establecimiento.objects.filter(direccion__icontains=query)[:10],
                        many=True)
                    establecimiento = {
                        "results": {
                            "category1": {
                                "name": "Nombre",
                                "results": establecimiento1.data
                            },
                            "category2": {
                                "name": "Direccion",
                                "results": establecimiento2.data
                            },
                            "query": query
                        }
                    }
                    return JSONResponse(establecimiento)
                else:
                    establecimiento = EstablecimientoSerializer(Establecimiento.objects.all(), many=True)
        return JSONResponse(establecimiento.data)


class InstitucionController(View):
    def get(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        if codigo_establecimiento:
            institucion = InstitucionSerializer(
                Institucion.objects.filter(codigo_establecimiento=codigo_establecimiento), many=True)
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
#     def get(self, request, *args, **kwargs):
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
