from django.conf.urls.i18n import i18n_patterns
from django.http import HttpResponseRedirect
from django.urls import include, path

urlpatterns = i18n_patterns(
    path('', lambda r: HttpResponseRedirect('common/')),

    path('common/', include('common.urls')),

    path('athletes/', include('athletes.urls')),
    path('clubs/', include('clubs.urls')),
    path('squads/', include('squads.urls')),
    path('streams/', include('streams.urls')),
    path('teams/', include('teams.urls')),
    path('tournaments/', include('tournaments.urls')),
)
