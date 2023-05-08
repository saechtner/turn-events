from django.urls import path, re_path

from squads import views

urlpatterns = [
    path("", views.index, name="squads.index"),
    path("new", views.SquadCreateView.as_view(), name="squads.new"),
    re_path(r"^(?P<slug>[-\w\d]*)-(?P<id>\d+)$", views.detail, name="squads.detail"),
    re_path(
        r"^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/edit$",
        views.SquadUpdateView.as_view(),
        name="squads.edit",
    ),
    re_path(
        r"^(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$",
        views.SquadDeleteView.as_view(),
        name="squads.delete",
    ),
    re_path(
        r"^(?P<slug>[-\w\d]*)-(?P<id>\d+)/assign_athletes$",
        views.assign_athletes,
        name="squads.assign_athletes",
    ),
    re_path(
        r"^(?P<slug>[-\w\d]*)-(?P<id>\d+)/enter_performances$",
        views.enter_performances,
        name="squads.enter_performances",
    ),
    re_path(
        r"^(?P<slug>[-\w\d]*)-(?P<id>\d+)/handle_entered_performances$",
        views.handle_entered_performances,
        name="squads.handle_entered_performances",
    ),
    re_path(r"^judge\.pdf$", views.create_judge_pdf, name="squads.create_judge_pdf"),
    re_path(
        r"^overview\.pdf$", views.create_overview_pdf, name="squads.create_overview_pdf"
    ),
]
