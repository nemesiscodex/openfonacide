from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from openfonacide.filtros import filtros, generar_ubicacion
from openfonacide.resumen import _resumen
from openfonacide.infografiaDNCP import *

from rest_framework import routers

from openfonacide.views import *


admin.autodiscover()

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'establecimientos', EstablecimientoViewSet)
router.register(r'instituciones', InstitucionViewSet)
router.register(r'espacios', EspacioViewSet)
router.register(r'mobiliarios', MobiliarioViewSet)
router.register(r'sanitarios', SanitarioViewSet)
router.register(r'serviciosbasicos', ServicioBasicoViewSet)

partial_patterns = patterns('',
    url(r'^registration/login\.html$', PartialGroupView.as_view(template_name='registration/login.html'), name='registration/login.html'),
    url(r'^registration/recuperar\.html$', PartialGroupView.as_view(template_name='registration/recuperar.html'), name='registration/recuperar.html'),
    url(r'^filtro-ubicacion\.html$', PartialGroupView.as_view(template_name='filtro-ubicacion.html'), name='filtro-ubicacion.html'),
    url(r'^footer\.html$', PartialGroupView.as_view(template_name='footer.html'), name='footer.html'),
    url(r'^map\.html$', PartialGroupView.as_view(template_name='map.html'), name='map.html'),
    url(r'^result-element\.html$', PartialGroupView.as_view(template_name='result-element.html'), name='result-element.html'),
    url(r'^results\.html$', PartialGroupView.as_view(template_name='results.html'), name='results.html'),
    url(r'^map-directive\.html$', PartialGroupView.as_view(template_name='map-directive.html'), name='map-directive.html'),
    url(r'^fonacide\.html$', PartialGroupView.as_view(template_name='fonacide.html'), name='fonacide.html'),
    url(r'^microplanificacion\.html$', PartialGroupView.as_view(template_name='microplanificacion.html'), name='microplanificacion.html'),
    url(r'^microplanificacion-proceso\.html$', PartialGroupView.as_view(template_name='microplanificacion-proceso.html'), name='microplanificacion-proceso.html'),
    url(r'^informacion\.html$', PartialGroupView.as_view(template_name='informacion.html'), name='informacion.html'),
    url(r'^graficos\.html$', PartialGroupView.as_view(template_name='graficos.html'), name='graficos.html'),
    url(r'^resumen\.html$', PartialGroupView.as_view(template_name='resumen.html'), name='resumen.html'),
    url(r'^login\.html$', PartialGroupView.as_view(template_name='login.html'), name='login.html'),
    url(r'^denuncia\.html$', PartialGroupView.as_view(template_name='denuncia.html'), name='denuncia.html'),
    url(r'^archivos-contraloria\.html$', PartialGroupView.as_view(template_name='archivos-contraloria.html'), name='archivos-contraloria.html'),
    url(r'^agregar-adjudicacion\.html$', PartialGroupView.as_view(template_name='agregar-adjudicacion.html'), name='agregar-adjudicacion.html'),
    url(r'^api\.html$', PartialGroupView.as_view(template_name='api.html'), name='api.html'),
    url(r'^institucion-list\.html$', PartialGroupView.as_view(template_name='institucion-list.html'), name='institucion-list.html'),
    url(r'^home\.html$', PartialGroupView.as_view(template_name='home.html'), name='home.html'),
    url(r'^search\.html$', PartialGroupView.as_view(template_name='search.html'), name='search.html'),
    url(r'^nav\.html$', PartialGroupView.as_view(template_name='nav.html'), name='nav.html'),
    url(r'^visualizaciones\.html$', PartialGroupView.as_view(template_name='visualizaciones.html'), name='visualizaciones.html'),
    url(r'^match\.html$', PartialGroupView.as_view(template_name='match.html'), name='match.html'),
    url(r'^acercade\.html$', PartialGroupView.as_view(template_name='acercade.html'), name='acercade.html'),
    url(r'^datasets\.html$', PartialGroupView.as_view(template_name='datasets.html'), name='datasets.html'),
    url(r'^legal\.html$', PartialGroupView.as_view(template_name='legal.html'), name='legal.html'),
   
    # ... more partials ...,
)

private_api = patterns('',
    url(r'^temporal/$', TemporalListView.as_view()),
    url(r'^unlink/$', UnlinkAPIView.as_view()),
)

"""
    XXX: Se puede mejorar el manejo de rutas, esto se hace para pasarle todas las rutas a router de
    AngularJS, particularmente la tercera ruta.
"""
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/v1/', include(router.urls)),
    url(r'^api/', include('rest_framework_swagger.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'index-nuevo.html'}),
    url(r'^accounts/recuperar/$', Recuperar.as_view(), name='recuperar_pass'),
    url(r'^(map/(?P<establecimiento>\d*)/?(?P<institucion>\d*)/?|fonacide|graficos|resumen|informacion|microplanificacion|microplanificacion-proceso|results|acercade|datasets|legal|match)?/?$', Index.as_view(), name='index'),
    # (.*)/? es para poder llamar desde cualquier lugar
    url(r'^((?!admin).)*/?partials/', include(partial_patterns, namespace='partials')),
    url(r'^((?!admin).)*/?prioridades/(?P<codigo_establecimiento>\w*)/?', PrioridadController.as_view(), name='prioridad'),
    url(r'^((?!admin).)*/?establecimiento/(?P<codigo_establecimiento>\w*)/?$', EstablecimientoController.as_view(), name='establecimiento'),
    url(r'^((?!admin).)*/?institucion/(?P<codigo_establecimiento>\w*)/?$', InstitucionController.as_view(), name='institucion'),
    # url(r'^listaInstituciones',ListaInstitucionesController.as_view(), name='listaInstituciones'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout',  {'next_page': 'index'}, name='logout'),
    url(r'^filtros/$', filtros, name='filtros'),
    url(r'^_resumen/$', _resumen, name='filtros'),
    url(r'^infografiaDNCP/$', infografiaDNCP, name='infografiaDNCP'),
    url(r'^agua$',   TemplateView.as_view(template_name='visualizaciones/agua.html'), name="agua"),
    url(r'^mobiliarios$',   TemplateView.as_view(template_name='visualizaciones/mobiliarios.html'), name="mobiliarios"),
    url(r'^dncp$',   TemplateView.as_view(template_name='visualizaciones/dncp.html'), name="dncp"),
    url(r'^ubicacion\.json$', generar_ubicacion, name='generar_ubicacion'),
    url(r'', include(private_api, namespace="private_api")),
    url(r'^estado_de_obra/?$', estado_de_obra, name='estado_de_obra'),
    url(r'^agregar_adjudicacion/?$', agregar_adjudicacion, name='agregar_adjudicacion')
)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = PartialGroupView.as_view(template_name='home.html')
