from django.conf.urls import url

from common import views

urlpatterns = [
    url(r'^$', views.index, name='home'),

    url(r'^disciplines/?$', views.disciplines_index, name='disciplines.index'),
    url(r'^disciplines/new$',
        views.DisciplineCreateView.as_view(), name='disciplines.new'),
    url(r'^disciplines/(?P<slug>[-\w\d]*)-(?P<id>\d+)$',
        views.discipline_detail, name='disciplines.detail'),
    url(r'^disciplines/(?P<slug>[-\w\d]*)-(?P<pk>\d+)/edit$',
        views.DisciplineUpdateView.as_view(), name='disciplines.edit'),
    url(r'^disciplines/(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$',
        views.DisciplineDeleteView.as_view(), name='disciplines.delete'),

    url(r'^performances/?$',
        views.performances_index, name='performances.index'),
    url(r'^performances/new$',
        views.PerformanceCreateView.as_view(), name='performances.new'),
    url(r'^performances/(?P<pk>\d+)$',
        views.PerformanceDetailView.as_view(), name='performances.detail'),
    url(r'^performances/(?P<pk>\d+)/edit$',
        views.PerformanceUpdateView.as_view(), name='performances.edit'),
    url(r'^performances/(?P<pk>\d+)/delete$',
        views.PerformanceDeleteView.as_view(), name='performances.delete'),
]
