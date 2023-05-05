from django.urls import path, re_path

from common import views

urlpatterns = [
    path("", views.index, name="home"),
    re_path(r"^disciplines/?$", views.disciplines_index, name="disciplines.index"),
    path(
        "disciplines/new",
        views.DisciplineCreateView.as_view(),
        name="disciplines.new",
    ),
    re_path(
        r"^disciplines/(?P<slug>[-\w\d]*)-(?P<id>\d+)$",
        views.discipline_detail,
        name="disciplines.detail",
    ),
    re_path(
        r"^disciplines/(?P<slug>[-\w\d]*)-(?P<pk>\d+)/edit$",
        views.DisciplineUpdateView.as_view(),
        name="disciplines.edit",
    ),
    re_path(
        r"^disciplines/(?P<slug>[-\w\d]*)-(?P<pk>\d+)/delete$",
        views.DisciplineDeleteView.as_view(),
        name="disciplines.delete",
    ),
    re_path(r"^performances/?$", views.performances_index, name="performances.index"),
    path(
        "performances/new",
        views.PerformanceCreateView.as_view(),
        name="performances.new",
    ),
    path(
        "performances/<int:pk>",
        views.PerformanceDetailView.as_view(),
        name="performances.detail",
    ),
    path(
        "performances/<int:pk>/edit",
        views.PerformanceUpdateView.as_view(),
        name="performances.edit",
    ),
    path(
        "performances/<int:pk>/delete",
        views.PerformanceDeleteView.as_view(),
        name="performances.delete",
    ),
]
