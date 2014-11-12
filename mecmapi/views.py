from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse

class Index(View):

    def get(self, request, *args, **kwargs):
        return render_to_response('test.html', context_instance=RequestContext(request))