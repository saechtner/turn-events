from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy
from django.views import generic

from common.models import Discipline, StreamDisciplineJoin
from streams.models import Stream
from utils.dict_operations import completed_performances


def index(request):
    context = { 'streams': Stream.objects.prefetch_related('athlete_set').all() }
    return render(request, 'gymnastics/streams/index.html', context)


def detail(request, id, slug):
    stream = Stream.objects \
        .prefetch_related('discipline_set') \
        .prefetch_related('athlete_set') \
        .prefetch_related('team_set__athlete_set__performance_set') \
        .get(id=id)

    disciplines = stream.get_ordered_disciplines()

    athletes = stream.athlete_set.all() \
        .select_related('club').select_related('stream').select_related('team__stream').select_related('squad') \
        .prefetch_related('performance_set')

    athletes_disciplines_result_dict = athletes.get_athletes_disciplines_result_dict()
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
        'athlete_performances_completed': completed_performances(athletes_disciplines_result_dict),
        'teams': teams,
        'teams_count': len(teams),
        'teams_disciplines_result_dict': teams_disciplines_result_dict,
        'teams_disciplines_rank_dict': teams_disciplines_rank_dict,
        'team_performances_completed': completed_performances(teams_disciplines_result_dict),
    }
    return render(request, 'gymnastics/streams/detail.html', context)


def new(request):
    if request.method == 'GET':
        context = { 'disciplines': Discipline.objects.all() }
        return render(request, 'gymnastics/streams/new.html', context)

    elif request.method == 'POST':
        stream = _build_stream_from_post(post_dict=request.POST)
        return redirect(stream.get_absolute_url())

    return HttpResponseNotAllowed(['GET', 'POST'])


def _build_stream_from_post(stream=None, post_dict={}, method='create'):
    disciplines = Discipline.objects.all()

    # check if selected disciplines exist
    try:
        selected_disciplines = [disciplines.get(id=discipline_id) for discipline_id in post_dict['chosen_list_order'].split()]
    except:
        # TODO fix missing request param
        return _abort_stream_creation(request, ugettext_lazy('Error: At least one discipline was not found.'))

    # check if difficulty was given (necessary)
    try:
        difficulty=post_dict['difficulty']
    except:
        # TODO fix missing request param
        return _abort_stream_creation(request, ugettext_lazy('Error: There is no difficulty given.'))

    if not stream:
        stream = Stream()

    # set values from
    stream.difficulty = difficulty
    stream.sex=post_dict.get('sex', 'f')
    stream.minimum_year_of_birth=int(post_dict.get('minimum_year_of_birth', 2000))
    stream.all_around_individual=post_dict.get('all_around_individual', False)
    stream.all_around_individual_counting_events=int(post_dict.get('all_around_individual_counting_events', 0)) \
        if stream.all_around_individual else 0
    stream.all_around_team=post_dict.get('all_around_team', False)
    stream.all_around_team_counting_athletes=int(post_dict.get('all_around_team_counting_athletes', 0)) \
        if stream.all_around_team else 0
    stream.discipline_finals=post_dict.get('discipline_finals', False)
    stream.discipline_finals_max_participants=int(post_dict.get('discipline_finals_max_participants', 0)) \
        if stream.discipline_finals else 0
    stream.discipline_finals_both_values_count=post_dict.get('discipline_finals_both_values_count', False)

    stream.save()

    if method == 'create':
        for position, discipline in enumerate(selected_disciplines):
            if discipline in stream.discipline_set.all():
                continue
            stream_discipline_join = StreamDisciplineJoin( \
                stream=stream,
                discipline=discipline,
                position=position
            )
            stream_discipline_join.save()
    elif method == 'update':
        stream_discipline_old_positions = stream.streamdisciplinejoin_set.all()
        for position, discipline in enumerate(selected_disciplines):
            stream_discipline_join = stream_discipline_old_positions.get(discipline=discipline)
            stream_discipline_join.position = position
            stream_discipline_join.save()
    else:
        # TODO fix missing request param
        return _abort_stream_creation(request, ugettext_lazy('Error: Unknown method.'))

    return stream


def _abort_stream_creation(request, error_message):
    if error_message:
        messages.error(request, error_message)

    context = { 'disciplines': Discipline.objects.all() }
    return render(request, 'gymnastics/streams/new.html', context)


def edit(request, id, slug):
    if request.method == 'GET':
        stream = Stream.objects.get(id=id)
        disciplines = stream.discipline_set.all()

        context = {
            'stream': stream,
            'stream_disciplines': stream.get_ordered_disciplines(),
            'disciplines': [discipline for discipline in Discipline.objects.all() if discipline not in disciplines],
        }
        return render(request, 'gymnastics/streams/edit.html', context)

    elif request.method == 'POST':
        stream = Stream.objects.get(id=id)
        _build_stream_from_post(stream=stream, post_dict=request.POST, method='update')
        return redirect(stream.get_absolute_url())

    return HttpResponseNotAllowed(['GET', 'POST'])


class StreamDeleteView(generic.DeleteView):

    model = Stream
    template_name = 'gymnastics/streams/delete.html'
    success_url = reverse_lazy('streams.index')
