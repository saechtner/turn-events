from django.conf.urls import patterns, include, url

from turnapp.controllers import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
