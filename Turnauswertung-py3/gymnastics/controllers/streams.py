from django.db.models import Sum
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.views import generic

from gymnastics.models import Stream


def index(request):
    context = { 'streams': Stream.objects.all() }
    return render(request, 'gymnastics/streams/index.html', context)

def detail(request, id):
    # TODO: sum function solved if len(disciplines) != counting_events

    # required objects and information ###
    # General: stream, stream.discipline_set
    stream = Stream.objects.select_related().get(id=id)
    disciplines = stream.discipline_set.all()

    # Athletes: stream.athlete_set
    athletes = stream.athlete_set.all() \
        .select_related('club').select_related('stream').select_related('team').select_related('squad') \
        .prefetch_related('performance_set') \
        .annotate(performances_result_total=Sum('performance__value'))


    # Results Athletes: stream.athlete_set + disciplines results + all_around result + ranks (sorted ...)
    athletes_discipline_results = stream.athlete_set.all() \
        .values('id', 'performance__discipline_id').annotate(performance_result=Sum('performance__value'))

    athletes_annotated_dict = { athlete.id: {} for athlete in athletes }
    for result in athletes_discipline_results:
        athletes_annotated_dict[result['id']][result['performance__discipline_id']] = result['performance_result']

    # Teams: stream.team_set
    teams = stream.team_set.all() \
        .select_related('stream').select_related('club') \
        .prefetch_related('athlete_set') \
        .annotate(performances_result_total=Sum('athlete__performance__value'))

    # Results Teams: stream.team_set + disciplines results + all_around result + ranks
    teams_discipline_results = stream.team_set.all() \
        .values('id', 'athlete__performance__discipline_id').annotate(performance_result=Sum('athlete__performance__value'))

    teams_annotated_dict = { team.id: {} for team in teams }
    for result in teams_discipline_results:
        teams_annotated_dict[result['id']][result['athlete__performance__discipline_id']] = result['performance_result']


    context = { 
        'stream': stream, 
        'disciplines': disciplines,
        'athletes': athletes,
        'athletes_annotated_dict': athletes_annotated_dict,
        'teams': teams,
        'teams_annotated_dict': teams_annotated_dict,
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
