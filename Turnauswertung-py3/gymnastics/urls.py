from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from gymnastics.controllers import views, athletes, clubs, disciplines, performances, squads, streams, teams
from gymnastics.controllers import athletes_imports

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'), 
    url(r'^todo$', views.todo, name='todo'),

    url(r'^athletes$', athletes.index, name='athletes.index'),
    url(r'^athletes/new$', athletes.AthleteCreateView.as_view(), name='athletes.new'),
    url(r'^athletes/results$', athletes.results, name='athletes.results'),
    url(r'^athletes/(?P<id>\d+)$', athletes.detail, name='athletes.detail'),
    url(r'^athletes/(?P<pk>\d+)/edit$', athletes.AthleteUpdateView.as_view(), name='athletes.edit'),
    url(r'^athletes/(?P<pk>\d+)/delete$', athletes.AthleteDeleteView.as_view(), name='athletes.delete'),

    url(r'^clubs$', clubs.index, name='clubs.index'),
    url(r'^clubs/new$', clubs.ClubCreateView.as_view(), name='clubs.new'),
    url(r'^clubs/(?P<id>\d+)$', clubs.detail, name='clubs.detail'),
    url(r'^clubs/(?P<pk>\d+)/edit$', clubs.ClubUpdateView.as_view(), name='clubs.edit'),
    url(r'^clubs/(?P<pk>\d+)/delete$', clubs.ClubDeleteView.as_view(), name='clubs.delete'),

    url(r'^disciplines$', disciplines.index, name='disciplines.index'),
    url(r'^disciplines/new$', disciplines.DisciplineCreateView.as_view(), name='disciplines.new'),
    url(r'^disciplines/(?P<id>\d+)$', disciplines.detail, name='disciplines.detail'),
    url(r'^disciplines/(?P<pk>\d+)/edit$', disciplines.DisciplineUpdateView.as_view(), name='disciplines.edit'),
    url(r'^disciplines/(?P<pk>\d+)/delete$', disciplines.DisciplineDeleteView.as_view(), name='disciplines.delete'),

    url(r'^performances$', performances.index, name='performances.index'),
    url(r'^performances/new$', performances.PerformanceCreateView.as_view(), name='performances.new'),
    url(r'^performances/(?P<pk>\d+)$', performances.PerformanceDetailView.as_view(), name='performances.detail'),
    url(r'^performances/(?P<pk>\d+)/edit$', performances.PerformanceUpdateView.as_view(), name='performances.edit'),
    url(r'^performances/(?P<pk>\d+)/delete$', performances.PerformanceDeleteView.as_view(), name='performances.delete'),

    url(r'^squads$', squads.index, name='squads.index'),
    url(r'^squads.handle_entered_performances$', squads.handle_entered_performances, name='squads.handle_entered_performances'),
    url(r'^squads/new$', squads.SquadCreateView.as_view(), name='squads.new'),
    url(r'^squads/(?P<id>\d+)$', squads.detail, name='squads.detail'),
    url(r'^squads/(?P<pk>\d+)/edit$', squads.SquadUpdateView.as_view(), name='squads.edit'),
    url(r'^squads/(?P<id>\d+)/enter_performances$', squads.enter_performances, name='squads.enter_performances'),
    url(r'^squads/(?P<pk>\d+)/delete$', squads.SquadDeleteView.as_view(), name='squads.delete'),

    url(r'^streams$', streams.index, name='streams.index'),
    url(r'^streams/new$', streams.StreamCreateView.as_view(), name='streams.new'),
    url(r'^streams/(?P<id>\d+)$', streams.detail, name='streams.detail'),
    url(r'^streams/(?P<pk>\d+)/edit$', streams.StreamUpdateView.as_view(), name='streams.edit'),
    url(r'^streams/(?P<pk>\d+)/delete$', streams.StreamDeleteView.as_view(), name='streams.delete'),

    url(r'^teams$', teams.index, name='teams.index'),
    url(r'^teams/new$', teams.TeamCreateView.as_view(), name='teams.new'),
    url(r'^teams/(?P<id>\d+)$', teams.detail, name='teams.detail'),
    url(r'^teams/(?P<pk>\d+)/edit$', teams.TeamUpdateView.as_view(), name='teams.edit'),
    url(r'^teams/(?P<pk>\d+)/delete$', teams.TeamDeleteView.as_view(), name='teams.delete'),

    url(r'^athletes_imports$', athletes_imports.index, name='athletes_imports.index'),
    url(r'^athletes_imports/new$', athletes_imports.new, name='athletes_imports.new'),
    url(r'^athletes_imports/(?P<id>\d+)$', athletes_imports.detail, name='athletes_imports.detail'),
    url(r'^athletes_imports/(?P<pk>\d+)/delete$', athletes_imports.DeleteView.as_view(), name='athletes_imports.delete'),
)
