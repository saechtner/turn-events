from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from gymnastics.controllers import views, clubs, disciplines, squads

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'), 

    url(r'^clubs$', clubs.index, name='clubs.index'),
    url(r'^clubs/new$', clubs.ClubCreateView.as_view(), name='clubs.new'),
    url(r'^clubs/(?P<pk>\d+)/detail', clubs.ClubDetailView.as_view(), name='clubs.detail'),
    url(r'^clubs/(?P<pk>\d+)/edit', clubs.ClubUpdateView.as_view(), name='clubs.edit'),
    url(r'^clubs/(?P<pk>\d+)/delete', clubs.ClubDeleteView.as_view(), name='clubs.delete'),

    url(r'^disciplines$', disciplines.index, name='disciplines.index'),
    url(r'^disciplines/new$', disciplines.DisciplineCreateView.as_view(), name='disciplines.new'),
    url(r'^disciplines/(?P<pk>\d+)/detail', disciplines.DisciplineDetailView.as_view(), name='disciplines.detail'),
    url(r'^disciplines/(?P<pk>\d+)/edit', disciplines.DisciplineUpdateView.as_view(), name='disciplines.edit'),
    url(r'^disciplines/(?P<pk>\d+)/delete', disciplines.DisciplineDeleteView.as_view(), name='disciplines.delete'),

    url(r'^squads$', squads.index, name='squads.index'),
    url(r'^squads/new$', squads.SquadCreateView.as_view(), name='squads.new'),
    url(r'^squads/(?P<pk>\d+)/detail', squads.SquadDetailView.as_view(), name='squads.detail'),
    url(r'^squads/(?P<pk>\d+)/edit', squads.SquadUpdateView.as_view(), name='squads.edit'),
    url(r'^squads/(?P<pk>\d+)/delete', squads.SquadDeleteView.as_view(), name='squads.delete'),
)

# urlpatterns += staticfiles_urlpatterns()
