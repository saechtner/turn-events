from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from gymnastics.models.squad import Squad


def index(request):
    context = { 'squads': Squad.objects.all() }
    return render(request, 'gymnastics/squads/index.html', context)


class SquadCreateView(generic.CreateView):

    model = Squad
    fields = ['name']
    template_name = 'gymnastics/squads/new.html'
    success_url = reverse_lazy('squads.index')


class SquadDetailView(generic.DetailView):

    model = Squad
    template_name = 'gymnastics/squads/detail.html'


class SquadUpdateView(generic.UpdateView):

    model = Squad
    fields = ['name']
    template_name = 'gymnastics/squads/edit.html'

    def get_success_url(self):
        some_kwargs = self.kwargs
        return reverse('squads.detail', kwargs = { 'pk' : self.kwargs['pk'] })


class SquadDeleteView(generic.DeleteView):

    model = Squad
    template_name = 'gymnastics/squads/delete.html'
    success_url = reverse_lazy('squads.index')
