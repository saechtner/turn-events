import re

from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from django.db.models import Sum

from gymnastics.models.athlete import Athlete
from gymnastics.models.discipline import Discipline
from gymnastics.models.performance import Performance
from gymnastics.models.squad import Squad
from gymnastics.models.stream import Stream


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
    streams_disctinct = set([athlete.stream for athlete in athletes])
    stream_athletes_disciplines = { stream.id: {'athletes': [], 'disciplines': stream.discipline_set.all()} for stream in streams_disctinct }
    for athlete in athletes:
        stream_athletes_disciplines[athlete.stream.id]['athletes'].append(athlete)

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
        'athletes_disciplines_result_dict': athletes_disciplines_result_dict,
        'streams': streams_disctinct,
        'stream_athletes_disciplines': stream_athletes_disciplines
    }
    return render(request, 'gymnastics/squads/detail.html', context)


def enter_performances(request, id):        
    squad = Squad.objects.get(id=id)

    #### Athletes ###
    athletes = squad.athlete_set.all() \
        .select_related('club').select_related('stream').select_related('team__stream').select_related('squad') \
        .prefetch_related('performance_set')

    ### Streams ###
    streams_disctinct = set([athlete.stream for athlete in athletes])
    stream_athletes_disciplines = { stream.id: {'athletes': [], 'disciplines': stream.discipline_set.all()} for stream in streams_disctinct }
    for athlete in athletes:
        stream_athletes_disciplines[athlete.stream.id]['athletes'].append(athlete)

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
        'athletes_disciplines_result_dict': athletes_disciplines_result_dict,
        'streams': streams_disctinct,
        'stream_athletes_disciplines': stream_athletes_disciplines
    }

    return render(request, 'gymnastics/squads/enter_performances.html', context)

def handle_entered_performances(request):
    performanceDict = request.POST

    athletes = Athlete.objects.all()
    disciplines = Discipline.objects.all()
    performances = Performance.objects.all()

    for key, value in performanceDict.items():
        if '-' in key and value:
            athleteID, performanceID = re.split(r'-+', key.rstrip())

            athlete = athletes.get(id=athleteID)
            discipline = disciplines.get(id=performanceID)

            try:
                performance = performances.get(athlete=athlete,discipline=discipline)
                performance.value = value
            except:
                performance = Performance( \
                    value=value,
                    athlete=athlete,
                    discipline=discipline
                )

            performance.save()

    return redirect(reverse('squads.index'))


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
        some_kwargs = self.kwargs
        return reverse('squads.detail', kwargs = { 'pk' : self.kwargs['pk'] })


class SquadDeleteView(generic.DeleteView):

    model = Squad
    template_name = 'gymnastics/squads/delete.html'
    success_url = reverse_lazy('squads.index')
