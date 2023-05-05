from django.urls import path, re_path

from tournaments import views

urlpatterns = [
    path('', views.index, name='tournaments.index'),
    path('main', views.main, name='tournaments.main'),
    path('new',
        views.TournamentCreateView.as_view(), name='tournaments.new'),
    re_path(r'^certificates\.pdf$', views.create_certificates_pdf,
        name='tournaments.create_certificates_pdf'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)/evaluation\.pdf$',
        views.create_evaluation_pdf, name='tournaments.create_evaluation_pdf'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)/solo_certificate_data\.txt$',
        views.create_solo_certificate_data_txt,
        name='tournaments.create_solo_certificate_data_txt'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)/team_certificate_data\.txt$',
        views.create_team_certificate_data_txt,
        name='tournaments.create_team_certificate_data_txt'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<id>\d+)$',
        views.detail, name='tournaments.detail'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/edit$',
        views.TournamentUpdateView.as_view(), name='tournaments.edit'),
    re_path(r'^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$',
        views.TournamentDeleteView.as_view(), name='tournaments.delete'),
]
