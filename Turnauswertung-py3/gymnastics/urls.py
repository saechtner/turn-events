from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from gymnastics.controllers import views, athletes, clubs, disciplines, performances, squads, streams, teams

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'), 
    url(r'^todo$', views.todo, name='todo'), 

    url(r'^athletes$', athletes.index, name='athletes.index'),
    url(r'^athletes/results$', athletes.results, name='athletes.results'),
    url(r'^athletes/new$', athletes.AthleteCreateView.as_view(), name='athletes.new'),
    url(r'^athletes/(?P<pk>\d+)/detail', athletes.AthleteDetailView.as_view(), name='athletes.detail'),

    url(r'^athletes/(?P<pk>\d+)/edit2', athletes.edit2, name='athletes.edit2'),
    url(r'^athletes/(?P<pk>\d+)/edit', athletes.AthleteUpdateView.as_view(), name='athletes.edit'),

    url(r'^athletes/(?P<pk>\d+)/delete', athletes.AthleteDeleteView.as_view(), name='athletes.delete'),

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

    url(r'^performances$', performances.index, name='performances.index'),
    url(r'^performances/new$', performances.PerformanceCreateView.as_view(), name='performances.new'),
    url(r'^performances/(?P<pk>\d+)/detail', performances.PerformanceDetailView.as_view(), name='performances.detail'),
    url(r'^performances/(?P<pk>\d+)/edit', performances.PerformanceUpdateView.as_view(), name='performances.edit'),
    url(r'^performances/(?P<pk>\d+)/delete', performances.PerformanceDeleteView.as_view(), name='performances.delete'),

    url(r'^squads$', squads.index, name='squads.index'),
    url(r'^squads/new$', squads.SquadCreateView.as_view(), name='squads.new'),
    url(r'^squads/(?P<pk>\d+)/detail', squads.SquadDetailView.as_view(), name='squads.detail'),
    url(r'^squads/(?P<pk>\d+)/edit', squads.SquadUpdateView.as_view(), name='squads.edit'),
    url(r'^squads/(?P<pk>\d+)/delete', squads.SquadDeleteView.as_view(), name='squads.delete'),

    url(r'^streams$', streams.index, name='streams.index'),
    url(r'^streams/new$', streams.StreamCreateView.as_view(), name='streams.new'),
    url(r'^streams/(?P<id>\d+)/detail', streams.detail, name='streams.detail'),
    url(r'^streams/(?P<pk>\d+)/edit', streams.StreamUpdateView.as_view(), name='streams.edit'),
    url(r'^streams/(?P<pk>\d+)/delete', streams.StreamDeleteView.as_view(), name='streams.delete'),

    url(r'^teams$', teams.index, name='teams.index'),
    url(r'^teams/new$', teams.TeamCreateView.as_view(), name='teams.new'),
    url(r'^teams/(?P<pk>\d+)/detail', teams.TeamDetailView.as_view(), name='teams.detail'),
    url(r'^teams/(?P<pk>\d+)/edit', teams.TeamUpdateView.as_view(), name='teams.edit'),
    url(r'^teams/(?P<pk>\d+)/delete', teams.TeamDeleteView.as_view(), name='teams.delete'),
)

# urlpatterns += staticfiles_urlpatterns()
