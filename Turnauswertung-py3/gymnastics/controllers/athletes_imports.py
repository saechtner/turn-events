import datetime
import re

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.views import generic

from gymnastics.models import Athlete, Club, Stream, Team
from gymnastics.models.athletes_import import AthletesImport


def index(request):
    context = { 'athletes_imports': AthletesImport.objects.all() }
    return render(request, 'gymnastics/athletes_imports/index.html', context)

def detail(request, id):
    athletes_import = AthletesImport.objects \
        .select_related('club') \
        .get(id=id)

    athletes = athletes_import.athlete_set.all() \
        .select_related('club').select_related('stream').select_related('team__stream').select_related('squad')

    context = { 
        'athletes_import': athletes_import,
        'athletes': athletes,
        'athletes_count': len(athletes),
    }
    return render(request, 'gymnastics/athletes_imports/detail.html', context)


def _parse_athlete_line(line, club, athletes_import):
    # TODO: idea - remove all return none and catch everything one level below

    elements = re.split(r'\t', line.rstrip())

    if len(elements) != 6 and len(elements) != 7:
        return None

    sex = 'm' if elements[5].lower().startswith('x') else Athlete._meta.get_field('sex').default

    date_of_birth_input = elements[2]
    if re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", date_of_birth_input): # English
        date_of_birth = datetime.date(int(date_of_birth_input[0:4]), int(date_of_birth_input[5:7]), int(date_of_birth_input[8:10]))
    elif re.match(r"^[0-9]{2}\.[0-9]{2}\.[0-9]{4}$", date_of_birth_input): # German
        date_of_birth = datetime.date(int(date_of_birth_input[6:10]), int(date_of_birth_input[3:5]), int(date_of_birth_input[0:2]))
    else:
        return None

    print(date_of_birth)

    stream_name = ''.join(elements[3].split()).upper() # remove all whitespace
    stream = None
    try:
        stream = Stream.objects.get(difficulty=stream_name, sex=sex)
        if date_of_birth.year < stream.minimum_year_of_birth:
            return None
    except:
        return None

    # TODO: handle teams during athletes import ... =/
    # team_name = elements[4])
    # teams = Team.objects.filter(club=club, stream=stream)
    # if teams:
    #     # search if the correct one is among them and use it, otherwise error or generate new one anyways
    # else:
    #     # generate them

    athlete = Athlete( \
            first_name=elements[0],
            last_name=elements[1],
            sex=sex,
            date_of_birth=date_of_birth,
            club=club,
            stream=stream,
            athletes_import=athletes_import)

    try:
        athlete.save()
    except:
        return None

    # TODO: Don't allow duplicates!!

    return athlete

def _abort_athletes_import(request, athletes_import, error_message):
    try:
        athletes_import.delete()
    except:
        pass

    if error_message:
        messages.error(request, error_message)

    context = { 'clubs': Club.objects.all() }
    return render(request, 'gymnastics/athletes_imports/new.html', context)


def new(request):
    # TODO: clean this up before it's too late

    if request.method == 'GET':
        selected_club_id = int(request.GET.get('club_id', -1))
        context = { 
            'clubs': Club.objects.all(),
            'selected_club_id': selected_club_id }
        return render(request, 'gymnastics/athletes_imports/new.html', context)

    elif request.method == 'POST':
        athletes_import = AthletesImport()
        athletes_list = []

        # check if a club was selected and thus exists in the database
        try:
            club = Club.objects.get(id=request.POST['club_id'])
            athletes_import.club = club
            athletes_import.save()
        except:
            return _abort_athletes_import(request, athletes_import, 'Error: No club selected.')

        # TODO: make sure there actually are lines
        if not request.POST['import_data']:
            return _abort_athletes_import(request, athletes_import, 'Error: No import data added.')

        lines = request.POST['import_data'].splitlines()
        if lines[0].startswith('Vorname\tN'):
            lines = lines[1:]
        for line in lines:
            athlete = _parse_athlete_line(line, club, athletes_import)
            athletes_list.append(athlete)

        if len(lines) > len(athletes_list):
            messages.warning(request, 'Warning: {0} objects were not created.'.format(len(lines) - len(athletes_list)))
        
        return redirect(reverse('athletes_imports.detail', kwargs={ 'id': athletes_import.id }))

    return HttpResponseNotAllowed(['GET', 'POST'])


class DeleteView(generic.DeleteView):

    model = AthletesImport
    template_name = 'gymnastics/athletes_imports/delete.html'
    success_url = reverse_lazy('athletes_imports.index')