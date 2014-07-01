from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings

from app.views import Registro, Actualizar, PerfilView

urlpatterns = patterns('',

    url(r'^$', 'app.views.home', name='home'),
    url(r'^ingresar/$', 'django.contrib.auth.views.login', {'template_name':'login.html'},name='login'),
    url(r'^salir/$', 'django.contrib.auth.views.logout_then_login',name='logout'),
    url(r'^registrarse/$', Registro.as_view(), name='registro'),
    url(r'^actualizar/$', Actualizar.as_view(), name='actualizar'),
    url(r'^perfil/(?P<pk>[-_\w]+)/$', PerfilView.as_view(), name='perfil'),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'^admin/', include(admin.site.urls)),
)
