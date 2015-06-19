from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns = i18n_patterns('',
    (r'^$', lambda r: HttpResponseRedirect('gymnastics/')),
    url(r'^gymnastics/', include('gymnastics.urls')), 
)