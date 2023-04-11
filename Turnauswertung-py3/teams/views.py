from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from teams.models import Team


def index(request):
    context = {
        'teams': Team.objects.all().select_related('club', 'stream')}
    return render(request, 'gymnastics/teams/index.html', context)


def detail(request, id):
    team = Team.objects.get(id=id)
    context = {
        'team': team,
        'club': team.club,
        'stream': team.stream }
    return render(request, 'gymnastics/teams/detail.html', context)


class TeamCreateView(generic.CreateView):

    model = Team
    fields = ['name', 'club', 'stream']
    template_name = 'gymnastics/teams/new.html'
    success_url = reverse_lazy('teams.index')


class TeamUpdateView(generic.UpdateView):

    model = Team
    fields = ['name', 'club', 'stream']
    template_name = 'gymnastics/teams/edit.html'

    def get_success_url(self):
        return reverse('teams.detail', kwargs={'id': self.kwargs['pk']})


class TeamDeleteView(generic.DeleteView):

    model = Team
    template_name = 'gymnastics/teams/delete.html'
    success_url = reverse_lazy('teams.index')
