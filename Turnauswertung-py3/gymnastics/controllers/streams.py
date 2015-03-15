from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from gymnastics.models.stream import Stream


def index(request):
    context = { 'streams': Stream.objects.all() }
    return render(request, 'gymnastics/streams/index.html', context)


class StreamCreateView(generic.CreateView):

    model = Stream
    fields = ['difficulty', 'sex', 'minimum_year_of_birth', 
        'all_around_individual', 'all_around_individual_counting_events', 
        'all_around_team', 'all_around_team_counting_athletes', 
        'discipline_finals', 'discipline_finals_max_participants', 'disciplines']
    template_name = 'gymnastics/streams/new.html'
    success_url = reverse_lazy('streams.index')


class StreamDetailView(generic.DetailView):

    model = Stream
    template_name = 'gymnastics/streams/detail.html'


class StreamUpdateView(generic.UpdateView):

    model = Stream
    fields = ['difficulty', 'sex', 'minimum_year_of_birth', 
        'all_around_individual', 'all_around_individual_counting_events', 
        'all_around_team', 'all_around_team_counting_athletes', 
        'discipline_finals', 'discipline_finals_max_participants', 'disciplines']
    template_name = 'gymnastics/streams/edit.html'

    def get_success_url(self):
        some_kwargs = self.kwargs
        return reverse('streams.detail', kwargs = { 'pk' : self.kwargs['pk'] })


class StreamDeleteView(generic.DeleteView):

    model = Stream
    template_name = 'gymnastics/streams/delete.html'
    success_url = reverse_lazy('streams.index')
