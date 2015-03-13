from django.conf.urls import patterns, include, url

from gymnastics.controllers import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
