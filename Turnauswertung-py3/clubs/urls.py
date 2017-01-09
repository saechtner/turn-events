from django.conf.urls import url

from clubs import views

urlpatterns = [
    url(r'^$', views.index, name='clubs.index'),
    url(r'^new$', views.ClubCreateView.as_view(), name='clubs.new'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)$',
        views.detail, name='clubs.detail'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/edit$',
        views.ClubUpdateView.as_view(), name='clubs.edit'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$',
        views.ClubDeleteView.as_view(), name='clubs.delete'),
]
