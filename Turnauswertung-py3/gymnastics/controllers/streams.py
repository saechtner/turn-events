from django.contrib import messages

from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.views import generic

from django.utils.translation import ugettext_lazy

from gymnastics.models import Stream, Discipline, StreamDisciplineJoin


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

    disciplines = stream.ordered_disciplines.all()

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

    context = { 'disciplines': Discipline.objects.all() }
    return render(request, 'gymnastics/streams/new.html', context)

def build_stream_from_post(stream=Stream(), post_dict={}, method='create'):
    disciplines = Discipline.objects.all()

    # check if selected disciplines exist
    try:
        selected_disciplines = [disciplines.get(id=discipline_id) for discipline_id in post_dict['chosen_list_order'].split()]
    except:
        return _abort_stream_creation(request, ugettext_lazy('Error: At least one discipline was not found.'))

    # check if difficulty was given (necessary)
    try:
        difficulty=post_dict['difficulty']
    except:
        return _abort_stream_creation(request, ugettext_lazy('Error: There is no difficulty given.'))

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
        return _abort_stream_creation(request, ugettext_lazy('Error: Unknown method.'))


    return stream


def new(request):
    if request.method == 'GET':
        context = { 'disciplines': Discipline.objects.all() }
        return render(request, 'gymnastics/streams/new.html', context)

    elif request.method == 'POST':
        stream = build_stream_from_post(post_dict=request.POST);
        return redirect(reverse('streams.detail', kwargs={ 'id': stream.id }))


def edit(request,id):
    if request.method == 'GET':
        stream = Stream.objects.get(id=id)

        context = { 
            'stream': stream,
            'stream_disciplines': stream.ordered_disciplines.all(),
            'disciplines': [discipline\
                            for discipline in Discipline.objects.all()\
                            if discipline not in stream.discipline_set.all()],
        }
        return render(request, 'gymnastics/streams/edit.html', context)

    elif request.method == 'POST':
        stream = Stream.objects.get(id=id)
        build_stream_from_post(stream=Stream.objects.get(id=id), post_dict=request.POST, method='update')
        return redirect(reverse('streams.detail', kwargs={ 'id': stream.id }))


class StreamDeleteView(generic.DeleteView):

    model = Stream
    template_name = 'gymnastics/streams/delete.html'
    success_url = reverse_lazy('streams.index')
