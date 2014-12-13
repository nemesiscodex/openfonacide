import datetime
import json
import urllib
import urllib2
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from mecmapi.models import *
from mecmapi.serializers import *


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
        return render_to_response('index.html', context_instance=RequestContext(request))


class ListaInstitucionesController(View):
    def get(self, request, *args, **kwargs):
        cantidad = request.GET.get('rows')
        pagina = request.GET.get('page')
        lista = InstitucionData.objects.all()
        if cantidad is not None:
            paginator = Paginator(lista, cantidad)
        else:
            paginator = Paginator(lista, 10)
        total = len(lista)
        if pagina is None:
            pagina = 1
        try:
            instituciones = paginator.page(pagina)
        except PageNotAnInteger:
            instituciones = paginator.page(1)
        except EmptyPage:
            instituciones = paginator.page(paginator.num_pages)
        lista_instituciones = ListaInstitucionesSerializer(instituciones, many=True)
        # result = lista_instituciones.data
        result = {'total': str(paginator.num_pages), 'page': pagina, 'records': str(total),
                  'rows': lista_instituciones.data}
        return JSONResponse(result)


class EstablecimientoController(View):
    def get(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        short = request.GET.get('short')
        query = request.GET.get('q')
        if short is not None:
            if codigo_establecimiento:
                establecimiento = EstablecimientoSerializerShort(
                    Institucion.objects.get(codigo_establecimiento=codigo_establecimiento))
            else:
                if query is not None:
                    establecimiento = EstablecimientoSerializerShort(
                        Institucion.objects.filter(nombre__icontains=query) |
                        Institucion.objects.filter(direccion__icontains=query), many=True)
                    establecimiento = {"results": establecimiento.data}
                    return JSONResponse(establecimiento)
                else:
                    establecimiento = EstablecimientoSerializerShort(Institucion.objects.all(), many=True)
        else:
            if codigo_establecimiento:
                establecimiento = EstablecimientoSerializer(
                    Institucion.objects.get(codigo_establecimiento=codigo_establecimiento))
            else:
                if query is not None:
                    establecimiento = EstablecimientoSerializer(Institucion.objects.filter(nombre__icontains=query) |
                                                                Institucion.objects.filter(direccion__icontains=query),
                                                                many=True)
                    establecimiento = {"results": establecimiento.data}
                    return JSONResponse(establecimiento)
                else:
                    establecimiento = EstablecimientoSerializer(Institucion.objects.all(), many=True)
        return JSONResponse(establecimiento.data)


class InstitucionController(View):
    def get(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        if codigo_establecimiento:
            institucion = InstitucionSerializer(
                InstitucionData.objects.filter(codigo_establecimiento=codigo_establecimiento), many=True)
        else:
            institucion = InstitucionSerializer(InstitucionData.objects.all(), many=True)
        return JSONResponse(institucion.data)


class PrioridadController(View):
    def get(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        result = {
            "construccion_aulas": get_P(codigo_establecimiento, ConstruccionAulas, ConstruccionAulasSerializer).data,
            "construccion_sanitarios": get_P(codigo_establecimiento, ConstruccionSanitario,
                                             ConstruccionSanitarioSerializer).data,
            "reparacion_aulas": get_P(codigo_establecimiento, ReparacionAulas, ReparacionAulasSerializer).data,
            "reparacion_sanitarios": get_P(codigo_establecimiento, ReparacionSanitario,
                                           ReparacionSanitarioSerializer).data
        }
        return JSONResponse(result)


class PrioridadControllerV2(View):
    def get(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        result = {
            "aulas": get_Pr(codigo_establecimiento, Espacios, EspaciosSerializer).data,
            "sanitarios": get_Pr(codigo_establecimiento, Sanitarios,
                                             SanitariosSerializer).data,
            "mobiliarios":get_Pr(codigo_establecimiento, Mobiliarios,
                                             MobiliariosSerializer).data,
           "estados":get_Pr(codigo_establecimiento, EstadosLocales,
                                             EstadosLocalesSerializer).data,


            
        
            
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
    def get(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        comentarios = Comentarios.objects.filter(codigo_establecimiento=codigo_establecimiento).order_by('fecha')
        return JSONResponse(ComentariosSerializer(comentarios, many=True).data)

    def post(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')

        captcha = json.loads(request.POST.get('captcha'))

        # captcha_result = urllib2.urlopen("https://www.google.com/recaptcha/api/siteverify",
        #                                  data=urllib.urlencode({
        #                                      "secret": "secret",
        #                                      "response": captcha
        #                                  })).read()

        # analize captcha result

        comentario = Comentarios()
        comentario.codigo_establecimiento_id = codigo_establecimiento
        comentario.autor = request.POST.get('autor')
        comentario.email = request.POST.get('email')
        comentario.texto = request.POST.get('texto')
        comentario.fecha = datetime.datetime.now()
        comentario.save()
        return JSONResponse({"success": True});