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


# line: Vorname      Name       Geb.    AK  Mannschaft  männlich    weiblich
# m/w in einer Spalte und männlich/weiblich als mögliche Werte ...
def _parse_athlete_line(line, club, athletes_import):
    # TODO: idea - remove all return none and catch everything one level below

    elements = re.split(r'\t', line.rstrip())

    if len(elements) != 6 and len(elements) != 7:
        return None

    sex = 'm' if elements[5].lower().startswith('x') else Athlete._meta.get_field('sex').default

    # date regex: 
    # ^\d{1,2}\/\d{1,2}\/\d{4}$
    # american date regex with lots of alternatives: 
    # ^[0,1]?\d{1}\/(([0-2]?\d{1})|([3][0,1]{1}))\/(([1]{1}[9]{1}[9]{1}\d{1})|([2-9]{1}\d{3}))$

    year_of_birth = elements[2]
    if not year_of_birth.isdigit():
        return None
    if len(year_of_birth) == 2:
        century_string = '20' if int(year_of_birth) < 60 else '19'
        year_of_birth = '{0}{1}'.format(century_string, year_of_birth)
    elif len(year_of_birth) != 4:
        return None

    stream_name = ''.join(elements[3].split()).upper() # remove all whitespace
    stream = None
    try:
        stream = Stream.objects.get(difficulty=stream_name, sex=sex)
        if int(year_of_birth) < stream.minimum_year_of_birth:
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
            year_of_birth=year_of_birth,
            club=club,
            stream=stream,
            athletes_import=athletes_import)

    try:
        athlete.save()
    except:
        return None

    # Don't allow duplicates!!

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
        messages.info(request, 'Keep in mind the following data structure: \
            First Name | Last Name | Sex | Year of Birth | Stream | Team.')

        try:
            selected_club_id = int(request.GET['club_id'])
        except: 
            selected_club_id = None

        context = { 
            'clubs': Club.objects.all(),
            'selected_club_id': selected_club_id }
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
            return _abort_athletes_import(request, athletes_import, 'Error: No club selected.')

        # TODO: make sure there actually are lines
        if not request.POST['import_data']:
            return _abort_athletes_import(request, athletes_import, 'Error: No import data added.')

        lines = request.POST['import_data'].splitlines()

        print(lines)

        if lines[0].startswith('Vorname\tN'):
            lines = lines[1:]
        for line in lines:
            athlete = _parse_athlete_line(line, club, athletes_import)
            athletes_list.append(athlete)

        if len(lines) > len(athletes_list):
            messages.warning(request, 'Warning: {0} objects were not created.'.format(len(lines) - len(athletes_list)))
        
        return redirect(reverse('athletes_imports.detail', kwargs={ 'id': athletes_import.id }))

    return  HttpResponseNotAllowed(['GET', 'POST'])