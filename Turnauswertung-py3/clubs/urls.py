from django.urls import path, re_path

from clubs import views

urlpatterns = [
    path('', views.index, name='clubs.index'),
    path('new', views.ClubCreateView.as_view(), name='clubs.new'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)$',
        views.detail, name='clubs.detail'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/edit$',
        views.ClubUpdateView.as_view(), name='clubs.edit'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$',
        views.ClubDeleteView.as_view(), name='clubs.delete'),
]
