from django.conf.urls import patterns, include, url
from django.contrib import admin

from mecmapi.views import Index, ListaInstitucionesController, EstablecimientoController, InstitucionController, PartialGroupView, PrioridadController

admin.autodiscover()

partial_patterns = patterns('',
    url(r'^footer\.html$', PartialGroupView.as_view(template_name='footer.html'), name='footer.html'),
    url(r'^api\.html$', PartialGroupView.as_view(template_name='api.html'), name='api.html'),
    url(r'^institucion-list\.html$', PartialGroupView.as_view(template_name='institucion-list.html'), name='institucion-list.html'),
    url(r'^home\.html$', PartialGroupView.as_view(template_name='home.html'), name='home.html'),
    url(r'^nav\.html$', PartialGroupView.as_view(template_name='nav.html'), name='nav.html'),
    url(r'^visualizaciones\.html$', PartialGroupView.as_view(template_name='visualizaciones.html'), name='visualizaciones.html'),
    url(r'^institucion-modal\.html$', PartialGroupView.as_view(template_name='institucion-modal.html'), name='institucion-modal.html'),
    url(r'^institucion-modal/establecimiento-tabla\.html$',
        PartialGroupView.as_view(template_name='institucion-modal/establecimiento-tabla.html'),
        name='institucion-modal/establecimiento-tabla.html'),
    url(r'^institucion-modal/instituciones-tabla\.html$',
        PartialGroupView.as_view(template_name='institucion-modal/instituciones-tabla.html'),
        name='institucion-modal/instituciones-tabla.html'),
  #  url(r'^institucion-modal/denuncias\.html$',
  #      PartialGroupView.as_view(template_name='institucion-modal/denuncias.html'),
  #      name='institucion-modal/denuncias.html'),
    url(r'^institucion-modal/comentarios\.html$',
        PartialGroupView.as_view(template_name='institucion-modal/comentarios.html'),
        name='institucion-modal/comentarios.html'),
    url(r'^institucion-modal/fonacide\.html$',
        PartialGroupView.as_view(template_name='institucion-modal/fonacide.html'),
        name='institucion-modal/fonacide.html'),
    # ... more partials ...,
)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^/?$', Index.as_view(), name='index'),
    url(r'^partials/', include(partial_patterns, namespace='partials')),
    url(r'^prioridades/(?P<codigo_establecimiento>\w*)/?', PrioridadController.as_view(), name=''),
    url(r'^establecimiento/(?P<codigo_establecimiento>\w*)/?$', EstablecimientoController.as_view(), name='establecimiento'),
    url(r'^institucion/(?P<codigo_establecimiento>\w*)/?$', InstitucionController.as_view(), name='institucion'),
    url(r'^listaInstituciones',ListaInstitucionesController.as_view(), name='listaInstituciones'),
    url(r'^admin/', include(admin.site.urls)),
)



