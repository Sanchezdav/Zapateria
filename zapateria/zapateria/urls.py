from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'app.views.home', name='home'),
    url(r'^ingresar/$', 'django.contrib.auth.views.login', {'template_name':'login.html'},name='login'),
    url(r'^salir/$', 'django.contrib.auth.views.logout_then_login',name='logout'),

    url(r'^admin/', include(admin.site.urls)),
)
