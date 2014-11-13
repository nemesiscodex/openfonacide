from django.conf.urls import patterns, include, url
from django.contrib import admin

from mecmapi.views import Index, InstitucionController

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^institucion/(?P<codigo_establecimiento>\w*)$', InstitucionController.as_view(), name='institucion'),
    url(r'^admin/', include(admin.site.urls)),
)



