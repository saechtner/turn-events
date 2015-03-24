from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from gymnastics.models.stream import Stream


def index(request):
    context = { 'streams': Stream.objects.all() }
    return render(request, 'gymnastics/streams/index.html', context)

def detail(request, id):
    # required objects and information ###
    # # General: stream, stream.discipline_set
    stream = Stream.objects.select_related().get(id=id)
    disciplines = stream.discipline_set.all()

    # # Athletes: stream.athlete_set
    athletes = stream.athlete_set.all() \
        .select_related('club').select_related('stream').select_related('team').select_related('squad') \
        .prefetch_related('performance_set')


    # # Results Athletes: stream.athlete_set + disciplines results + all_around result + ranks (sorted ...)


    # # Teams: stream.team_set
    teams = stream.team_set.all() \
        .select_related('stream').select_related('club') \
        .prefetch_related('athlete_set')

    # # Results Teams: stream.team_set + disciplines results + all_around result + ranks


    context = { 
        'stream': stream, 
        'athletes': athletes,
        'teams': teams,
        'athletes_all_around_rank_dict': stream.athletes_all_around_rank_dict,
        'teams_all_around_rank_dict': stream.teams_all_around_rank_dict
    }
    return render(request, 'gymnastics/streams/detail.html', context)


class StreamCreateView(generic.CreateView):

    model = Stream
    fields = ['difficulty', 'sex', 'minimum_year_of_birth', 
        'all_around_individual', 'all_around_individual_counting_events', 
        'all_around_team', 'all_around_team_counting_athletes', 
        'discipline_finals', 'discipline_finals_max_participants', 
        'discipline_finals_both_values_count', 'discipline_set']
    template_name = 'gymnastics/streams/new.html'
    success_url = reverse_lazy('streams.index')


class StreamUpdateView(generic.UpdateView):

    model = Stream
    fields = ['difficulty', 'sex', 'minimum_year_of_birth', 
        'all_around_individual', 'all_around_individual_counting_events', 
        'all_around_team', 'all_around_team_counting_athletes', 
        'discipline_finals', 'discipline_finals_max_participants', 
        'discipline_finals_both_values_count', 'discipline_set']
    template_name = 'gymnastics/streams/edit.html'

    def get_success_url(self):
        some_kwargs = self.kwargs
        return reverse('streams.detail', kwargs = { 'id' : self.kwargs['pk'] })


class StreamDeleteView(generic.DeleteView):

    model = Stream
    template_name = 'gymnastics/streams/delete.html'
    success_url = reverse_lazy('streams.index')
