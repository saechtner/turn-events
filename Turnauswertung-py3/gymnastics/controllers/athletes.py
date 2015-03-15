from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from gymnastics.models.athlete import Athlete


def index(request):
    context = { 'athletes': Athlete.objects.all() }
    return render(request, 'gymnastics/athletes/index.html', context)


class AthleteCreateView(generic.CreateView):

    model = Athlete
    fields = ['first_name', 'last_name', 'sex', 'year_of_birth', 'club', 'squad', 'stream', 'team']
    template_name = 'gymnastics/athletes/new.html'
    success_url = reverse_lazy('athletes.index')


class AthleteDetailView(generic.DetailView):

    model = Athlete
    template_name = 'gymnastics/athletes/detail.html'


class AthleteUpdateView(generic.UpdateView):

    model = Athlete
    fields = ['first_name', 'last_name', 'sex', 'year_of_birth', 'club', 'squad', 'stream', 'team']
    template_name = 'gymnastics/athletes/edit.html'

    def get_success_url(self):
        some_kwargs = self.kwargs
        return reverse('athletes.detail', kwargs = { 'pk' : self.kwargs['pk'] })


class AthleteDeleteView(generic.DeleteView):

    model = Athlete
    template_name = 'gymnastics/athletes/delete.html'
    success_url = reverse_lazy('athletes.index')
