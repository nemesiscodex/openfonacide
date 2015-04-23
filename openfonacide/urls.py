from django.conf.urls import patterns, include, url
from django.contrib import admin
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
    url(r'^footer\.html$', PartialGroupView.as_view(template_name='footer.html'), name='footer.html'),
    url(r'^map\.html$', PartialGroupView.as_view(template_name='map.html'), name='map.html'),
    url(r'^map-directive\.html$', PartialGroupView.as_view(template_name='map-directive.html'), name='map-directive.html'),
    url(r'^fonacide\.html$', PartialGroupView.as_view(template_name='fonacide.html'), name='fonacide.html'),
    url(r'^graficos\.html$', PartialGroupView.as_view(template_name='graficos.html'), name='graficos.html'),
    url(r'^resumen\.html$', PartialGroupView.as_view(template_name='resumen.html'), name='resumen.html'),
    url(r'^login\.html$', PartialGroupView.as_view(template_name='login.html'), name='login.html'),
    url(r'^denuncia\.html$', PartialGroupView.as_view(template_name='denuncia.html'), name='denuncia.html'),
    url(r'^archivos-contraloria\.html$', PartialGroupView.as_view(template_name='archivos-contraloria.html'), name='archivos-contraloria.html'),
    url(r'^api\.html$', PartialGroupView.as_view(template_name='api.html'), name='api.html'),
    url(r'^institucion-list\.html$', PartialGroupView.as_view(template_name='institucion-list.html'), name='institucion-list.html'),
    url(r'^home\.html$', PartialGroupView.as_view(template_name='home.html'), name='home.html'),
    url(r'^search\.html$', PartialGroupView.as_view(template_name='search.html'), name='search.html'),
    url(r'^nav\.html$', PartialGroupView.as_view(template_name='nav.html'), name='nav.html'),
    url(r'^visualizaciones\.html$', PartialGroupView.as_view(template_name='visualizaciones.html'), name='visualizaciones.html'),
    url(r'^institucion-modal\.html$', PartialGroupView.as_view(template_name='institucion-modal.html'), name='institucion-modal.html'),
    url(r'^institucion-modal/establecimiento-tabla\.html$',
        PartialGroupView.as_view(template_name='institucion-modal/establecimiento-tabla.html'),
        name='institucion-modal/establecimiento-tabla.html'),
    url(r'^institucion-modal/instituciones-tabla\.html$',
        PartialGroupView.as_view(template_name='institucion-modal/instituciones-tabla.html'),
        name='institucion-modal/instituciones-tabla.html'),
    url(r'^institucion-modal/instituciones-tabs/aulas\.html$',
        PartialGroupView.as_view(template_name='institucion-modal/instituciones-tabs/aulas.html'),
        name='institucion-modal/aulas.html'),
    url(r'^institucion-modal/instituciones-tabs/denuncias\.html$',
        PartialGroupView.as_view(template_name='institucion-modal/instituciones-tabs/denuncias.html'),
        name='institucion-modal/denuncias.html'),
    url(r'^institucion-modal/instituciones-tabs/mobiliarios\.html$',
        PartialGroupView.as_view(template_name='institucion-modal/instituciones-tabs/mobiliarios.html'),
        name='institucion-modal/mobiliarios.html'),
    url(r'^institucion-modal/instituciones-tabs/sanitarios\.html$',
        PartialGroupView.as_view(template_name='institucion-modal/instituciones-tabs/sanitarios.html'),
        name='institucion-modal/sanitarios.html'),
    url(r'^institucion-modal/instituciones-tabs/informacion\.html$',
        PartialGroupView.as_view(template_name='institucion-modal/instituciones-tabs/informacion.html'),
        name='institucion-modal/informacion.html'),
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

    url(r'^api/v1/', include(router.urls)),
    url(r'^api/', include('rest_framework_swagger.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'index-nuevo.html'}),
    url(r'^accounts/recuperar/$', Recuperar.as_view(), name='recuperar_pass'),
    url(r'^(map/(?P<establecimiento>\d*)/?(?P<institucion>\d*)/?|fonacide|graficos|resumen)?/?$', Index.as_view(), name='index'),
    # (.*)/? es para poder llamar desde cualquier lugar
    url(r'^((?!admin).)*/?partials/', include(partial_patterns, namespace='partials')),
    url(r'^((?!admin).)*/?prioridades/(?P<codigo_establecimiento>\w*)/?', PrioridadController.as_view(), name='prioridad'),
    url(r'^comentarios/(?P<codigo_establecimiento>\w+)/?', ComentariosController.as_view(), name='comentarios'),
    url(r'^((?!admin).)*/?establecimiento/(?P<codigo_establecimiento>\w*)/?$', EstablecimientoController.as_view(), name='establecimiento'),
    url(r'^((?!admin).)*/?institucion/(?P<codigo_establecimiento>\w*)/?$', InstitucionController.as_view(), name='institucion'),
    # url(r'^listaInstituciones',ListaInstitucionesController.as_view(), name='listaInstituciones'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout',  {'next_page': 'index'}, name='logout'),
)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

# handler404 = PartialGroupView.as_view(template_name='home.html')
