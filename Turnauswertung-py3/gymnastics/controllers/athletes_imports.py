import re

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.views import generic

from gymnastics.models import Athlete, Club, Stream, Team
from gymnastics.models.athletes_import import AthletesImport


def index(request):
    context = { 'athletes_imports': AthletesImport.objects.all() }
    return render(request, 'gymnastics/athletes_imports/index.html', context)

def detail(request, id):
    context = { 'athletes_import': AthletesImport.objects.get(id=id) }
    return render(request, 'gymnastics/athletes_imports/detail.html', context)


class DeleteView(generic.DeleteView):

    model = AthletesImport
    template_name = 'gymnastics/athletes_imports/delete.html'
    success_url = reverse_lazy('athletes_imports.index')


def _parse_athlete_line(line, club, athletes_import):
    elements = re.split(r'\t+', line.rstrip())
    if len(elements) != 5 and len(elements) != 6:
        return None

    sex = 'm' if elements[2].lower().startswith('m') else Athlete._meta.get_field('sex').default

    year_of_birth = elements[3]
    if len(year_of_birth) == 2:
        year_of_birth = '20{0}'.format(year_of_birth)
    elif len(year_of_birth) != 4:
        return None
    try:
        year_of_birth = int(year_of_birth)
    except:
        return None

    stream_name = ''.join(elements[4].split()).upper() # remove all whitespace
    stream = None
    try:
        stream = Stream.objects.get(difficulty=stream_name, sex=sex)
        if stream.minimum_year_of_birth > year_of_birth:
            return None
    except:
        return None

    # TODO: handle teams during athletes import ... =/
    # team_name = elements[5])
    # teams = Team.objects.filter(club=club, stream=stream)
    # if teams:
    #     # search if the correct one is among them and use it, otherwise error or generate new one anyways
    # else:
    #     # generate them

    athlete = Athlete( \
            first_name=elements[0],
            last_name=elements[1],
            sex=sex,
            year_of_birth=year_of_birth,
            club=club,
            stream=stream,
            athletes_import=athletes_import
        )

    try:
        athlete.save()
    except:
        return None

    # Don't allow duplicates!!

    return athlete

def abort_athletes_import(request, athletes_import, error_message):
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
        messages.info(request, 'Keep in mind the following data structure: \
            First Name | Last Name | Sex | Year of Birth | Stream | Team.')

        context = { 'clubs': Club.objects.all() }
        return render(request, 'gymnastics/athletes_imports/new.html', context)

    elif request.method == 'POST':
        athletes_import = AthletesImport()
        athletes_list = []

        # check if a club was selected and thus it exists in the datbase
        try:
            club = Club.objects.get(id=request.POST['club_id'])
            athletes_import.club = club
            athletes_import.save()
        except:
            return abort_athletes_import(request, athletes_import, 'Error: No club selected.')

        # TODO: make sure there actually are lines
        if not request.POST['import_data']:
            return abort_athletes_import(request, athletes_import, 'Error: No import data added.')

        lines = request.POST['import_data'].splitlines()
        if lines[0].startswith('Vorname\tNachname'):
            lines = lines[1:]
        for line in lines:
            athlete = _parse_athlete_line(line, club, athletes_import)
            athletes_list.append(athlete)

        if len(lines) > len(athletes_list):
            messages.warning(request, 'Warning: {0} objects were not created.'.format(len(lines) - len(athletes_list)))
        
        return redirect(reverse('athletes_imports.detail', kwargs={ 'id': athletes_import.id }))