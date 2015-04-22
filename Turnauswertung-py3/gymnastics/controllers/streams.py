from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.views import generic

from django.utils.translation import ugettext_lazy as _

from gymnastics.models import Stream
from gymnastics.models import Discipline


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


def new(request):
    # TODO: clean this up before it's too late

    if request.method == 'GET':
        context = { 
            'disciplines': Discipline.objects.all(),
        }
        return render(request, 'gymnastics/streams/new.html', context)

    elif request.method == 'POST':
        # athletes_import = AthletesImport()
        # athletes_list = []

        # # check if a club was selected and thus it exists in the datbase
        # try:
        #     club = Club.objects.get(id=request.POST['club_id'])
        #     athletes_import.club = club
        #     athletes_import.save()
        # except:
        #     return _abort_athletes_import(request, athletes_import, 'Error: No club selected.')

        # # TODO: make sure there actually are lines
        # if not request.POST['import_data']:
        #     return _abort_athletes_import(request, athletes_import, 'Error: No import data added.')

        # lines = request.POST['import_data'].splitlines()
        # if lines[0].startswith('Vorname\tNachname'):
        #     lines = lines[1:]
        # for line in lines:
        #     athlete = _parse_athlete_line(line, club, athletes_import)
        #     athletes_list.append(athlete)

        # if len(lines) > len(athletes_list):
        #     messages.warning(request, 'Warning: {0} objects were not created.'.format(len(lines) - len(athletes_list)))
        
        # return redirect(reverse('athletes_imports.detail', kwargs={ 'id': athletes_import.id }))

        context = { 
            'disciplines': Discipline.objects.all(),
        }
        
        return render(request, 'gymnastics/streams/new.html', context)


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
