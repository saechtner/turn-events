import re

from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Sum
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.utils.translation import ugettext_lazy
from django.views import generic

from utils import pdf
from athletes.models import Athlete
from squads.models import Squad
from gymnastics.models import Performance
from utils.dict_operations import completed_performances


def index(request):
    context = {'squads': Squad.objects.all()}
    return render(request, 'gymnastics/squads/index.html', context)


def detail(request, id, slug):
    squad = Squad.objects.get(id=id)

    athletes = squad.athlete_set.order_by('squad_position') \
        .select_related('club').select_related('stream').select_related('team__stream').select_related('squad') \
        .prefetch_related('performance_set')        
    athletes_disciplines_result_dict = athletes.get_athletes_disciplines_result_dict()

    streams_distinct = athletes.get_distinct_stream_set()
    stream_athletes_dict = squad.get_stream_athletes_dict(athletes)
    stream_disciplines_dict = squad.get_stream_disciplines_dict(athletes)

    context = { 
        'squad': squad,
        'athletes': athletes,
        'athletes_count': len(athletes),
        'streams': streams_distinct,
        'stream_athletes_dict': stream_athletes_dict,
        'stream_disciplines_dict': stream_disciplines_dict,
        'athletes_disciplines_result_dict': athletes_disciplines_result_dict,
        'performances_completed': completed_performances(athletes_disciplines_result_dict),
    }
    return render(request, 'gymnastics/squads/detail.html', context)


def assign_athletes(request, id, slug):
    squad = Squad.objects.get(id=id)

    if request.method == 'GET':
        squad_athletes = squad.athlete_set.order_by('squad_position') \
            .select_related('club').select_related('stream')
        non_squad_athletes = Athlete.objects.filter(squad=None) \
            .select_related('club').select_related('stream').select_related('team__stream').select_related('squad')

        context = { 
            'squad': squad,
            'squad_athletes': squad_athletes,
            'non_squad_athletes': non_squad_athletes,
        }
        return render(request, 'gymnastics/squads/assign_athletes.html', context)

    elif request.method == 'POST':
        old_squad_athletes = squad.athlete_set.all() \
            .select_related('squad')
        for athlete in old_squad_athletes:
            athlete.squad = None
            athlete.squad_position = Athlete._meta.get_field('squad_position').default
            athlete.save()

        new_squad_athletes = [Athlete.objects.get(id=athlete_id) for athlete_id in request.POST['chosen_list_order'].split()]
        for position, athlete in enumerate(new_squad_athletes):
            athlete.squad = squad
            athlete.squad_position = position
            athlete.save()

        return redirect(reverse('squads.index'))

    return HttpResponseNotAllowed(['GET', 'POST'])


def enter_performances(request, id, slug):
    squad = Squad.objects.get(id=id)

    #### Athletes ###
    athletes = squad.athlete_set.order_by('squad_position') \
        .select_related('club').select_related('stream').select_related('team__stream').select_related('squad') \
        .prefetch_related('performance_set')

    ### Streams ###
    streams_distinct = athletes.get_distinct_stream_set()
    stream_athletes_dict = squad.get_stream_athletes_dict(athletes)
    stream_disciplines_dict = squad.get_stream_disciplines_dict(athletes)

    stream_discipline_tabindex_dict = { 
        stream.id: { 
            discipline.id: 10 * stream_index + discipline_index \
                for discipline_index, discipline in enumerate(stream.get_ordered_disciplines()) 
        } for stream_index, stream in enumerate(streams_distinct, start=1) 
    }

    # Results Athletes: disciplines results
    athletes_discipline_results = squad.athlete_set.all() \
        .values('id', 'performance__discipline_id') \
        .annotate(performance_result=Sum('performance__value'))
    athletes_disciplines_result_dict = { athlete.id: {} for athlete in athletes }
    for result in athletes_discipline_results:
        athletes_disciplines_result_dict[result['id']][result['performance__discipline_id']] = result['performance_result']

    context = { 
        'squad': squad,
        'streams': streams_distinct,
        'stream_athletes_dict': stream_athletes_dict,
        'stream_disciplines_dict': stream_disciplines_dict,
        'stream_discipline_tabindex_dict': stream_discipline_tabindex_dict,
        'athletes_disciplines_result_dict': athletes_disciplines_result_dict,
    }

    return render(request, 'gymnastics/squads/enter_performances.html', context)


def handle_entered_performances(request):
    performances = Performance.objects.all()

    for key, value in request.POST.items():
        if '-' in key and value:
            athlete_id, discipline_id = re.split('-', key.rstrip())

            try:
                performance = performances.get(athlete_id=athlete_id, discipline_id=discipline_id)
            except:
                performance = Performance(athlete_id=athlete_id, discipline_id=discipline_id)
            val = float(value.replace(',', '.'))
            if val <= 20.0 or val >= 0.0:
                performance.value = val
            performance.save()

    return redirect(reverse('squads.index'))


def create_judge_pdf(request):
    squads = Squad.objects.all() \
        .prefetch_related('athlete_set') \
        .select_related('athlete_set__stream')

    squad_athletes_dict = { 
        squad.id: squad.athlete_set.order_by('squad_position').select_related('stream') for squad in squads
    }

    squad_difficulty_indices = { squad.id: {} for squad in squads }
    for squad in squads:
        previous_athlete = None
        athletes_in_stream = 0
        for athlete in squad_athletes_dict[squad.id]:
            if previous_athlete and athlete.stream != previous_athlete.stream:
                squad_difficulty_indices[squad.id][previous_athlete.id] = athletes_in_stream
                athletes_in_stream = 0
            athletes_in_stream += 1
            previous_athlete = athlete
        squad_difficulty_indices[squad.id][previous_athlete.id] = athletes_in_stream

    squad_disciplines_dict = { squad.id: squad.get_disciplines(squad.athlete_set.all()) for squad in squads }

    context = {
        'squads': squads,
        'squad_disciplines_dict': squad_disciplines_dict,
        'squad_athletes_dict': squad_athletes_dict,
        'squad_difficulty_indices': squad_difficulty_indices,
    }
    template_location = 'gymnastics/documents/squads_judges.tex'
    file_name = '{0}_{1}_{2}.pdf'.format(ugettext_lazy('Squads'), ugettext_lazy('Judge'), ugettext_lazy('Lists'))

    return pdf.create(template_location, context, file_name)


def create_overview_pdf(request):
    squads = Squad.objects.all() \
        .prefetch_related('athlete_set') \
        .select_related('athlete_set__club') \
        .select_related('athlete_set__team__stream')

    squad_athletes_dict = { 
        squad.id: squad.athlete_set.order_by('squad_position') \
            .select_related('club').select_related('team__stream')
        for squad in squads }

    context = {
        'squads': squads,
        'squad_athletes_dict': squad_athletes_dict,
    }
    template_location = 'gymnastics/documents/squads_athletes.tex'
    file_name = '{0}_{1}.pdf'.format(ugettext_lazy('Squads'), ugettext_lazy('Overview'))

    return pdf.create(template_location, context, file_name)


class SquadCreateView(generic.CreateView):

    model = Squad
    fields = ['name']
    template_name = 'gymnastics/squads/new.html'


class SquadUpdateView(generic.UpdateView):

    model = Squad
    fields = ['name']
    template_name = 'gymnastics/squads/edit.html'


class SquadDeleteView(generic.DeleteView):

    model = Squad
    template_name = 'gymnastics/squads/delete.html'
    success_url = reverse_lazy('squads.index')
