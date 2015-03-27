from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from gymnastics.models.discipline import Discipline


def index(request):
    context = { 'disciplines': Discipline.objects.all() }
    return render(request, 'gymnastics/disciplines/index.html', context)


def detail(request, id):
    discipline = Discipline.objects.get(id=id)
    streams = discipline.stream_set.all()
    performances = discipline.performance_set.all().select_related('athlete')

    context = { 
        'discipline': discipline,
        'streams': streams,
        'performances': performances
    }
    return render(request, 'gymnastics/disciplines/detail.html', context)


class DisciplineCreateView(generic.CreateView):

    model = Discipline
    fields = ['name']
    template_name = 'gymnastics/disciplines/new.html'
    success_url = reverse_lazy('disciplines.index')


class DisciplineUpdateView(generic.UpdateView):

    model = Discipline
    fields = ['name']
    template_name = 'gymnastics/disciplines/edit.html'

    def get_success_url(self):
        some_kwargs = self.kwargs
        return reverse('disciplines.detail', kwargs = { 'pk' : self.kwargs['pk'] })


class DisciplineDeleteView(generic.DeleteView):

    model = Discipline
    template_name = 'gymnastics/disciplines/delete.html'
    success_url = reverse_lazy('disciplines.index')
