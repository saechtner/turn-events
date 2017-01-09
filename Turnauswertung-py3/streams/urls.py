from django.conf.urls import url

from streams import views

urlpatterns = [
    url(r'^$', views.index, name='streams.index'),
    url(r'^new$', views.new, name='streams.new'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)$',
        views.detail, name='streams.detail'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)/edit$',
        views.edit, name='streams.edit'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$',
        views.StreamDeleteView.as_view(), name='streams.delete'),
]
