from django.urls import path, re_path

from athletes import views

urlpatterns = [
    path('', views.index_athletes, name='athletes.index'),
    path('new', views.AthleteCreateView.as_view(), name='athletes.new'),
    path('results', views.results, name='athletes.results'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)$',
        views.detail_athlete, name='athletes.detail'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/edit$',
        views.AthleteUpdateView.as_view(), name='athletes.edit'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$',
        views.AthleteDeleteView.as_view(), name='athletes.delete'),

    re_path(r'^imports/?$', views.index, name='athletes_imports.index'),
    path('imports/new', views.new, name='athletes_imports.new'),
    path('imports/<int:id>',
        views.detail, name='athletes_imports.detail'),
    path('imports/<int:pk>/delete',
        views.DeleteView.as_view(), name='athletes_imports.delete'),
]
