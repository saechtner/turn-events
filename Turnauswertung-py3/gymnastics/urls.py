from django.conf.urls import patterns, include, url

from gymnastics.controllers import disciplines

urlpatterns = patterns('',
    url(r'^disciplines$', disciplines.index, name='disciplines.index'),
    url(r'^disciplines/new$', disciplines.DisciplineCreateView.as_view(), name='disciplines.new'),
    url(r'^disciplines/(?P<pk>\d+)/detail', disciplines.DisciplineDetailView.as_view(), name='disciplines.detail'),
    url(r'^disciplines/(?P<pk>\d+)/edit', disciplines.DisciplineUpdateView.as_view(), name='disciplines.edit'),
    url(r'^disciplines/(?P<pk>\d+)/delete', disciplines.DisciplineDeleteView.as_view(), name='disciplines.delete'),
)
