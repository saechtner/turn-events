from django.urls import path, re_path

from streams import views

urlpatterns = [
    path('', views.index, name='streams.index'),
    path('new', views.new, name='streams.new'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)$',
        views.detail, name='streams.detail'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)/edit$',
        views.edit, name='streams.edit'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$',
        views.StreamDeleteView.as_view(), name='streams.delete'),
]
