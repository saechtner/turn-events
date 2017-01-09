from django.conf.urls import url

from tournaments import views

urlpatterns = [
    url(r'^$', views.index, name='tournaments.index'),
    url(r'^main$', views.main, name='tournaments.main'),
    url(r'^new$',
        views.TournamentCreateView.as_view(), name='tournaments.new'),
    url(r'^certificates\.pdf$', views.create_certificates_pdf,
        name='tournaments.create_certificates_pdf'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)/evaluation\.pdf$',
        views.create_evaluation_pdf, name='tournaments.create_evaluation_pdf'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)/solo_certificate_data\.txt$',
        views.create_solo_certificate_data_txt,
        name='tournaments.create_solo_certificate_data_txt'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)/team_certificate_data\.txt$',
        views.create_team_certificate_data_txt,
        name='tournaments.create_team_certificate_data_txt'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)$',
        views.detail, name='tournaments.detail'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/edit$',
        views.TournamentUpdateView.as_view(), name='tournaments.edit'),
    url(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$',
        views.TournamentDeleteView.as_view(), name='tournaments.delete'),
]
