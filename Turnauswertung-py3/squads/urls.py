from django.conf.urls import url

from squads import views

urlpatterns = [
    url(r'^$', views.index, name='squads.index'),
    url(r'^judge\.pdf$', views.create_judge_pdf, name='squads.create_judge_pdf'),
    url(r'^overview\.pdf$',
        views.create_overview_pdf, name='squads.create_overview_pdf'),
    url(r'^handle_entered_performances$',
        views.handle_entered_performances,
        name='squads.handle_entered_performances'),
    url(r'^new$', views.SquadCreateView.as_view(), name='squads.new'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)$',
        views.detail, name='squads.detail'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/edit$',
        views.SquadUpdateView.as_view(), name='squads.edit'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)/assign_athletes$',
        views.assign_athletes, name='squads.assign_athletes'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)/enter_performances$',
        views.enter_performances, name='squads.enter_performances'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$',
        views.SquadDeleteView.as_view(), name='squads.delete'),
]
