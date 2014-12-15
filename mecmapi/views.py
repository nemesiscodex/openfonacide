import datetime
import json
import urllib
import urllib2
from django.views.decorators.gzip import gzip_page
from django.http import StreamingHttpResponse
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
from itertools import chain
from operator import attrgetter
import json
import csv
import os


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

class ListaPrioridadesController(View):
    def get(self, request, *args, **kwargs):
        cantidad = request.GET.get('iDisplayLength')
        inicio = request.GET.get('iDisplayStart')
        cantidad_columnas = request.GET.get('iColumns')
        order_by = request.GET.get('iSortCol_0')
        order_dir = request.GET.get('sSortDir_0')
        filtro = {}
        columnas = []
        for i in range(int(cantidad_columnas)):
            valor = request.GET.get('sSearch_'+str(i))
            columnas.append(request.GET.get('mDataProp_'+str(i))) 
            if valor :
                filtro[ columnas[i] + "__icontains"] = valor
        print filtro
        if filtro != "" :
            lista_const_aulas = ConstruccionAulas.objects.filter(**filtro)
            lista_const_sanitarios = ConstruccionSanitario.objects.filter(**filtro)
            lista_rep_aulas = ReparacionAulas.objects.filter(**filtro)
            lista_rep_sanitarios = ReparacionSanitario.objects.filter(**filtro)
        else :
            lista_const_aulas = ConstruccionAulas.objects.all()
            lista_const_sanitarios = ConstruccionSanitario.objects.all()
            lista_rep_aulas = ReparacionAulas.objects.all()
            lista_rep_sanitarios = ReparacionSanitario.objects.all()
        if order_by != "0":
            if order_dir == "asc" :
                lista = sorted(chain(lista_const_aulas, lista_const_sanitarios, lista_rep_aulas, lista_rep_sanitarios),
                    key=attrgetter(columnas[int(order_by)]))
            else :
                lista = sorted(chain(lista_const_aulas, lista_const_sanitarios, lista_rep_aulas, lista_rep_sanitarios),
                    key=attrgetter(columnas[int(order_by)]), reverse=True)
        else :
            if order_dir == "asc" :
                lista = sorted(chain(lista_const_aulas, lista_const_sanitarios, lista_rep_aulas, lista_rep_sanitarios),
                    key=attrgetter('departamento', 'prioridad'))
            else :
                lista = sorted(chain(lista_const_aulas, lista_const_sanitarios, lista_rep_aulas, lista_rep_sanitarios),
                    key=attrgetter('departamento', 'prioridad'), reverse=True)
        pagina = int(inicio)/int(cantidad) + 1
        if cantidad is not None :
            paginator = Paginator(lista, cantidad)
        else :
            paginator = Paginator(lista, 10)
        total = len(lista)
        if pagina is None :
            pagina = 1
        try :
            prioridades = paginator.page(pagina)
        except PageNotAnInteger:
            prioridades = paginator.page(1)
        except EmptyPage :
            prioridades = paginator.page(paginator.num_pages)
        lista_prioridades = ListaPrioridadesSerializer(prioridades, many=True)
        result = { 'recordsFiltered' : str(total), 'identificador' : str(pagina), 'recordsTotal': str(total), 'data': lista_prioridades.data }
        return JSONResponse(result)

class DescargasController(View):
    def get(self,request, *args, **kwargs):
        archivo = request.GET.get('archivo')
        path  = "static/csv/"+archivo+".csv"
        response = StreamingHttpResponse(open(path),content_type='text/csv')
        response['Content-Disposition'] = "attachment; filename="+ archivo +".csv"
        return response



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