from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from mecmapi.models import Institucion
from mecmapi.serializers import InstitucionesSerializer


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
        return render_to_response('test.html', context_instance=RequestContext(request))


class InstitucionController(View):
    def get(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        if codigo_establecimiento:
            instituciones = InstitucionesSerializer(Institucion.objects.filter(codigo_establecimiento=codigo_establecimiento), many=True)
        else:
            instituciones = InstitucionesSerializer(Institucion.objects.all(), many=True)
        return JSONResponse(instituciones.data)
