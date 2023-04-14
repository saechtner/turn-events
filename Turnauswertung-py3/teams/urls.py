from django.urls import path, re_path

from teams import views

urlpatterns = [
    re_path(r'^teams/?$', views.index, name='teams.index'),
    path('teams/new', views.TeamCreateView.as_view(), name='teams.new'),
    path('teams/<int:id>', views.detail, name='teams.detail'),
    path('teams/<int:pk>/edit',
        views.TeamUpdateView.as_view(), name='teams.edit'),
    path('teams/<int:pk>/delete',
        views.TeamDeleteView.as_view(), name='teams.delete'),
]
