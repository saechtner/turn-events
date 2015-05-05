import re

from django.db.models import Sum
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.utils.translation import ugettext_lazy
from django.views import generic

from gymnastics.models.athlete import Athlete
from gymnastics.models.discipline import Discipline
from gymnastics.models.performance import Performance
from gymnastics.models.squad import Squad
from gymnastics.models.stream import Stream
from gymnastics.utils import pdf


def index(request):
    context = { 'squads': Squad.objects.all() }
    return render(request, 'gymnastics/squads/index.html', context)

def detail(request, id):
    squad = Squad.objects.get(id=id)

    #### Athletes ###
    athletes = squad.athlete_set.all() \
        .select_related('club').select_related('stream').select_related('team__stream').select_related('squad') \
        .prefetch_related('performance_set')

    ### Streams ###
    streams_distinct = set([athlete.stream for athlete in athletes])
    stream_athletes_dict = squad.get_stream_athletes_dict(athletes)
    stream_disciplines_dict = squad.get_stream_disciplines_dict(athletes)

    # Results Athletes: disciplines results
    athletes_discipline_results = squad.athlete_set.all() \
        .values('id', 'performance__discipline_id') \
        .annotate(performance_result=Sum('performance__value'))
    athletes_disciplines_result_dict = { athlete.id: {} for athlete in athletes }
    for result in athletes_discipline_results:
        athletes_disciplines_result_dict[result['id']][result['performance__discipline_id']] = result['performance_result']

    context = { 
        'squad': squad,
        'athletes': athletes,
        'athletes_count': len(athletes),
        'streams': streams_distinct,
        'stream_athletes_dict': stream_athletes_dict,
        'stream_disciplines_dict': stream_disciplines_dict,
        'athletes_disciplines_result_dict': athletes_disciplines_result_dict,
    }
    return render(request, 'gymnastics/squads/detail.html', context)

def enter_performances(request, id):        
    squad = Squad.objects.get(id=id)

    #### Athletes ###
    athletes = squad.athlete_set.all() \
        .select_related('club').select_related('stream').select_related('team__stream').select_related('squad') \
        .prefetch_related('performance_set')

    ### Streams ###
    streams_distinct = set([athlete.stream for athlete in athletes])
    stream_athletes_dict = squad.get_stream_athletes_dict(athletes)
    stream_disciplines_dict = squad.get_stream_disciplines_dict(athletes)

    stream_discipline_tabindex_dict = { 
        stream.id: { 
            discipline.id: 10 * stream_index + discipline_index \
                for discipline_index, discipline in enumerate(stream.ordered_disciplines.all()) 
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

            performance.value = value
            performance.save()

    return redirect(reverse('squads.index'))

def create_judge_pdf(request):
    squads = Squad.objects.all() \
        .prefetch_related('athlete_set') \
        .select_related('athlete_set__stream')
    
    squad_athletes_dict = {}
    squad_disciplines_dict = {}
    for squad in squads:
        athletes = squad.athlete_set.all()
        squad_athletes_dict[squad.id] = athletes
        squad_disciplines_dict[squad.id] = squad.get_disciplines(athletes)

    context = {
        'squads': squads,
        'squad_disciplines_dict': squad_disciplines_dict,
        'squad_athletes_dict': squad_athletes_dict,
    }
    template_location = 'gymnastics/squads/squads_judges.tex'
    file_name = '{0}_{1}_{2}.pdf'.format(ugettext_lazy('Squads'), ugettext_lazy('Judge'), ugettext_lazy('Lists'))

    return pdf.create(template_location, context, file_name)

def create_overview_pdf(request):
    squads = Squad.objects.all() \
        .prefetch_related('athlete_set') \
        .select_related('athlete_set__club')

    context = {
        'squads': squads,
    }
    template_location = 'gymnastics/squads/squads_athletes.tex'
    file_name = '{0}_{1}.pdf'.format(ugettext_lazy('Squads'), ugettext_lazy('Overview'))

    return pdf.create(template_location, context, file_name)


class SquadCreateView(generic.CreateView):

    model = Squad
    fields = ['name']
    template_name = 'gymnastics/squads/new.html'
    success_url = reverse_lazy('squads.index')


class SquadUpdateView(generic.UpdateView):

    model = Squad
    fields = ['name']
    template_name = 'gymnastics/squads/edit.html'

    def get_success_url(self):
        return reverse('squads.detail', kwargs = { 'id' : self.kwargs['pk'] })


class SquadDeleteView(generic.DeleteView):

    model = Squad
    template_name = 'gymnastics/squads/delete.html'
    success_url = reverse_lazy('squads.index')
