from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.gzip import gzip_page
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from mecmapi.models import Institucion, InstitucionData
from mecmapi.serializers import EstablecimientoSerializer, EstablecimientoSerializerShort, InstitucionSerializer


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


class EstablecimientoController(View):
    def get(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        short = request.GET.get('short')
        if short is not None:
            if codigo_establecimiento:
                establecimiento = EstablecimientoSerializerShort(Institucion.objects.get(codigo_establecimiento=codigo_establecimiento))
            else:
                establecimiento = EstablecimientoSerializerShort(Institucion.objects.all(), many=True)
        else:
            if codigo_establecimiento:
                establecimiento = EstablecimientoSerializer(Institucion.objects.get(codigo_establecimiento=codigo_establecimiento))
            else:
                establecimiento = EstablecimientoSerializer(Institucion.objects.all(), many=True)
        return JSONResponse(establecimiento.data)


class InstitucionController(View):
    def get(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        if codigo_establecimiento:
            institucion = InstitucionSerializer(InstitucionData.objects.filter(codigo_establecimiento=codigo_establecimiento), many=True)
        else:
            institucion = InstitucionSerializer(InstitucionData.objects.all(), many=True)
        return JSONResponse(institucion.data)
