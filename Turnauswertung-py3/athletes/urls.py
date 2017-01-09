from django.conf.urls import url

from athletes import views

urlpatterns = [
    url(r'^/?$', views.index_athletes, name='athletes.index'),
    url(r'^new$', views.AthleteCreateView.as_view(), name='athletes.new'),
    url(r'^results$', views.results, name='athletes.results'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)$',
        views.detail_athlete, name='athletes.detail'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/edit$',
        views.AthleteUpdateView.as_view(), name='athletes.edit'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$',
        views.AthleteDeleteView.as_view(), name='athletes.delete'),

    url(r'^imports/?$', views.index, name='athletes_imports.index'),
    url(r'^imports/new$', views.new, name='athletes_imports.new'),
    url(r'^imports/(?P<id>\d+)$',
        views.detail, name='athletes_imports.detail'),
    url(r'^imports/(?P<pk>\d+)/delete$',
        views.DeleteView.as_view(), name='athletes_imports.delete'),
]
