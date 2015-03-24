from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from gymnastics.models.performance import Performance


def index(request):
    context = { 'performances': Performance.objects.all() \
        .select_related('athlete').select_related('discipline') }
    return render(request, 'gymnastics/performances/index.html', context)


class PerformanceCreateView(generic.CreateView):

    model = Performance
    fields = ['athlete', 'discipline', 'value', 'value_final']
    template_name = 'gymnastics/performances/new.html'
    success_url = reverse_lazy('performances.index')


class PerformanceDetailView(generic.DetailView):

    model = Performance
    template_name = 'gymnastics/performances/detail.html'


class PerformanceUpdateView(generic.UpdateView):

    model = Performance
    fields = ['athlete', 'discipline', 'value', 'value_final']
    template_name = 'gymnastics/performances/edit.html'

    def get_success_url(self):
        some_kwargs = self.kwargs
        return reverse('performances.detail', kwargs = { 'pk' : self.kwargs['pk'] })


class PerformanceDeleteView(generic.DeleteView):

    model = Performance
    template_name = 'gymnastics/performances/delete.html'
    success_url = reverse_lazy('performances.index')
