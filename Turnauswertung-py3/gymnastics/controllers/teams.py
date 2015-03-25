from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from gymnastics.models.team import Team


def index(request):
    context = { 'teams': Team.objects.all().select_related('club').select_related('stream') }
    return render(request, 'gymnastics/teams/index.html', context)


def detail(request, id):
    team = Team.objects.get(id=id)
    club = team.club
    stream = team.stream
    context = { 
        'team': team,
        'club': club,
        'stream': stream }
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
        some_kwargs = self.kwargs
        return reverse('teams.detail', kwargs = { 'pk' : self.kwargs['pk'] })


class TeamDeleteView(generic.DeleteView):

    model = Team
    template_name = 'gymnastics/teams/delete.html'
    success_url = reverse_lazy('teams.index')
