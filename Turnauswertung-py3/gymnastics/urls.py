from django.conf.urls import patterns, include, url

from gymnastics.controllers import disciplines

urlpatterns = patterns('',
    url(r'^$', disciplines.index, name='index')
)
