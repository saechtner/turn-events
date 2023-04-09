from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += i18n_patterns(
    url(r'^$', lambda r: HttpResponseRedirect('common/')),

    url(r'^common/', include('common.urls')),

    url(r'^athletes/', include('athletes.urls')),
    url(r'^clubs/', include('clubs.urls')),
    url(r'^squads/', include('squads.urls')),
    url(r'^streams/', include('streams.urls')),
    url(r'^teams/', include('teams.urls')),
    url(r'^tournaments/', include('tournaments.urls')),
)
