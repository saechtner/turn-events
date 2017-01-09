from django.conf.urls import url

from gymnastics.views import views, disciplines, performances, squads, streams, teams, tournaments

urlpatterns = [
    url(r'^$', views.index, name='home'),

    url(r'^disciplines/?$', disciplines.index, name='disciplines.index'),
    url(r'^disciplines/new$', disciplines.DisciplineCreateView.as_view(), name='disciplines.new'),
    url(r'^disciplines/(?P<slug>[-\w\d]*)-(?P<id>\d+)$', disciplines.detail, name='disciplines.detail'),
    url(r'^disciplines/(?P<slug>[-\w\d]*)-(?P<pk>\d+)/edit$', disciplines.DisciplineUpdateView.as_view(), name='disciplines.edit'),
    url(r'^disciplines/(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$', disciplines.DisciplineDeleteView.as_view(), name='disciplines.delete'),

    url(r'^performances/?$', performances.index, name='performances.index'),
    url(r'^performances/new$', performances.PerformanceCreateView.as_view(), name='performances.new'),
    url(r'^performances/(?P<pk>\d+)$', performances.PerformanceDetailView.as_view(), name='performances.detail'),
    url(r'^performances/(?P<pk>\d+)/edit$', performances.PerformanceUpdateView.as_view(), name='performances.edit'),
    url(r'^performances/(?P<pk>\d+)/delete$', performances.PerformanceDeleteView.as_view(), name='performances.delete'),

    url(r'^squads/?$', squads.index, name='squads.index'),
    url(r'^squads/judge\.pdf$', squads.create_judge_pdf, name='squads.create_judge_pdf'),
    url(r'^squads/overview\.pdf$', squads.create_overview_pdf, name='squads.create_overview_pdf'),
    url(r'^squads/handle_entered_performances$', squads.handle_entered_performances, name='squads.handle_entered_performances'),
    url(r'^squads/new$', squads.SquadCreateView.as_view(), name='squads.new'),
    url(r'^squads/(?P<slug>[-\w\d]*)-(?P<id>\d+)$', squads.detail, name='squads.detail'),
    url(r'^squads/(?P<slug>[-\w\d]*)-(?P<pk>\d+)/edit$', squads.SquadUpdateView.as_view(), name='squads.edit'),
    url(r'^squads/(?P<slug>[-\w\d]*)-(?P<id>\d+)/assign_athletes$', squads.assign_athletes, name='squads.assign_athletes'),
    url(r'^squads/(?P<slug>[-\w\d]*)-(?P<id>\d+)/enter_performances$', squads.enter_performances, name='squads.enter_performances'),
    url(r'^squads/(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$', squads.SquadDeleteView.as_view(), name='squads.delete'),

    url(r'^streams/?$', streams.index, name='streams.index'),
    url(r'^streams/new$', streams.new, name='streams.new'),
    url(r'^streams/(?P<slug>[-\w\d]*)-(?P<id>\d+)$', streams.detail, name='streams.detail'),
    url(r'^streams/(?P<slug>[-\w\d]*)-(?P<id>\d+)/edit$', streams.edit, name='streams.edit'),
    url(r'^streams/(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$', streams.StreamDeleteView.as_view(), name='streams.delete'),

    url(r'^teams/?$', teams.index, name='teams.index'),
    url(r'^teams/new$', teams.TeamCreateView.as_view(), name='teams.new'),
    url(r'^teams/(?P<id>\d+)$', teams.detail, name='teams.detail'),
    url(r'^teams/(?P<pk>\d+)/edit$', teams.TeamUpdateView.as_view(), name='teams.edit'),
    url(r'^teams/(?P<pk>\d+)/delete$', teams.TeamDeleteView.as_view(), name='teams.delete'),

    url(r'^tournaments/?$', tournaments.index, name='tournaments.index'),
    url(r'^tournaments/main$', tournaments.main, name='tournaments.main'),
    url(r'^tournaments/new$', tournaments.TournamentCreateView.as_view(), name='tournaments.new'),
    url(r'^tournaments/certificates\.pdf$', tournaments.create_certificates_pdf, name='tournaments.create_certificates_pdf'),
    url(r'^tournaments/(?P<slug>[-\w\d]*)-(?P<id>\d+)/evaluation\.pdf$', tournaments.create_evaluation_pdf, name='tournaments.create_evaluation_pdf'),
    url(r'^tournaments/(?P<slug>[-\w\d]*)-(?P<id>\d+)/solo_certificate_data\.txt$', tournaments.create_solo_certificate_data_txt, name='tournaments.create_solo_certificate_data_txt'),
    url(r'^tournaments/(?P<slug>[-\w\d]*)-(?P<id>\d+)/team_certificate_data\.txt$', tournaments.create_team_certificate_data_txt, name='tournaments.create_team_certificate_data_txt'),
    url(r'^tournaments/(?P<slug>[-\w\d]*)-(?P<id>\d+)$', tournaments.detail, name='tournaments.detail'),
    url(r'^tournaments/(?P<slug>[-\w\d]*)-(?P<pk>\d+)/edit$', tournaments.TournamentUpdateView.as_view(), name='tournaments.edit'),
    url(r'^tournaments/(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$', tournaments.TournamentDeleteView.as_view(), name='tournaments.delete'),
]
