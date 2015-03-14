from django.conf.urls import patterns, include, url

from gymnastics.controllers import clubs, disciplines

urlpatterns = patterns('',
    url(r'^clubs$', clubs.index, name='clubs.index'),
    url(r'^clubs/new$', clubs.ClubCreateView.as_view(), name='clubs.new'),
    url(r'^clubs/(?P<pk>\d+)/detail', clubs.ClubDetailView.as_view(), name='clubs.detail'),
    url(r'^clubs/(?P<pk>\d+)/edit', clubs.ClubUpdateView.as_view(), name='clubs.edit'),
    url(r'^clubs/(?P<pk>\d+)/delete', clubs.ClubDeleteView.as_view(), name='clubs.delete'),url(r'^disciplines$', disciplines.index, name='disciplines.index'),
    url(r'^disciplines/new$', disciplines.DisciplineCreateView.as_view(), name='disciplines.new'),
    url(r'^disciplines/(?P<pk>\d+)/detail', disciplines.DisciplineDetailView.as_view(), name='disciplines.detail'),
    url(r'^disciplines/(?P<pk>\d+)/edit', disciplines.DisciplineUpdateView.as_view(), name='disciplines.edit'),
    url(r'^disciplines/(?P<pk>\d+)/delete', disciplines.DisciplineDeleteView.as_view(), name='disciplines.delete'),
)
