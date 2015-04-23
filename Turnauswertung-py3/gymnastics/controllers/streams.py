from django.contrib import messages

from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.views import generic

from django.utils.translation import ugettext_lazy as _

from gymnastics.models import Stream
from gymnastics.models import Discipline
from gymnastics.models import StreamDisciplineJoin


def index(request):
    context = { 'streams': Stream.objects.all() }
    return render(request, 'gymnastics/streams/index.html', context)

def detail(request, id):
    stream = Stream.objects \
        .prefetch_related('discipline_set') \
        .prefetch_related('team_set') \
            .prefetch_related('team_set__athlete_set') \
            .prefetch_related('team_set__athlete_set__performance_set') \
        .prefetch_related('athlete_set') \
            .prefetch_related('athlete_set__performance_set') \
        .get(id=id)

    disciplines = stream.discipline_set.all()

    athletes = stream.athlete_set.all() \
        .select_related('club').select_related('stream').select_related('team__stream').select_related('squad') \
        .prefetch_related('performance_set') \
        .prefetch_related('stream__discipline_set')

    athletes_disciplines_result_dict = stream.get_athletes_disciplines_result_dict()
    athletes_disciplines_rank_dict = stream.get_athletes_disciplines_rank_dict(athletes_disciplines_result_dict)

    teams = stream.team_set.all() \
        .select_related('stream').select_related('club') \
        .prefetch_related('athlete_set')

    teams_disciplines_result_dict = stream.get_teams_disciplines_result_dict()
    teams_disciplines_rank_dict = stream.get_teams_disciplines_rank_dict(teams_disciplines_result_dict)

    context = { 
        'stream': stream, 
        'disciplines': disciplines,
        'athletes': athletes,
        'athletes_count': len(athletes),
        'athletes_disciplines_result_dict': athletes_disciplines_result_dict,
        'athletes_disciplines_rank_dict': athletes_disciplines_rank_dict,
        'teams': teams,
        'teams_disciplines_result_dict': teams_disciplines_result_dict,
        'teams_disciplines_rank_dict': teams_disciplines_rank_dict,}
    return render(request, 'gymnastics/streams/detail.html', context)

def _abort_stream_creation(request, error_message):
    if error_message:
        messages.error(request, error_message)
        
    context = { 
        'disciplines': Discipline.objects.all(),
    }
    return render(request, 'gymnastics/streams/new.html', context)


def new(request):
    # TODO: clean this up before it's too late

    if request.method == 'GET':
        context = { 
            'disciplines': Discipline.objects.all(),
        }
        return render(request, 'gymnastics/streams/new.html', context)

    elif request.method == 'POST':
        all_disciplines = Discipline.objects.all()

        # check if selected disciplines exist
        try:
            disciplines = [all_disciplines.get(id=discipline_id) for discipline_id in request.POST['chosen_list_order'].split()]
        except:
            return _abort_stream_creation(request, _('Error: At least one discipline was not found.'))

        try:
            difficulty=request.POST['difficulty']
        except:
            return _abort_stream_creation(request, _('Error: There is no difficulty given.'))



        stream = Stream( \
            difficulty=difficulty,
            sex=request.POST.get('sex', 'f'),
            minimum_year_of_birth=int(request.POST.get('minimum_year_of_birth', '2000')),
            all_around_individual=request.POST.get('all_around_individual', True),
            all_around_individual_counting_events=int(request.POST.get('all_around_individual_counting_events', 0)),
            all_around_team=request.POST.get('all_around_team', False),
            all_around_team_counting_athletes=int(request.POST.get('all_around_team_counting_athletes', 0)),
            discipline_finals=request.POST.get('discipline_finals', False),
            discipline_finals_max_participants=int(request.POST.get('discipline_finals_max_participants', 0)),
            discipline_finals_both_values_count=request.POST.get('discipline_finals_both_values_count', False),
        )
        stream.save()

        position = 1
        for discipline in disciplines:
            stream_discipline_join = StreamDisciplineJoin( \
                stream=stream,
                discipline=discipline,
                position=position
            )
            stream_discipline_join.save()
            position += 1
        
        return redirect(reverse('streams.detail', kwargs={ 'id': stream.id }))


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
