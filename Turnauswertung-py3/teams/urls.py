from django.conf.urls import url

from teams import views

urlpatterns = [
    url(r'^teams/?$', views.index, name='teams.index'),
    url(r'^teams/new$', views.TeamCreateView.as_view(), name='teams.new'),
    url(r'^teams/(?P<id>\d+)$', views.detail, name='teams.detail'),
    url(r'^teams/(?P<pk>\d+)/edit$',
        views.TeamUpdateView.as_view(), name='teams.edit'),
    url(r'^teams/(?P<pk>\d+)/delete$',
        views.TeamDeleteView.as_view(), name='teams.delete'),
]
