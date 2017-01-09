import json
import datetime
import re

from django.http import HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.views import generic

from athletes.models import Athlete, AthletesImport
from gymnastics.models import Club, Stream, Team


def index_athletes(request):
    context = {
        'athletes': Athlete.objects.select_related(
            'club', 'stream', 'team__stream', 'squad'
        ).all()
    }
    return render(request, 'gymnastics/athletes/index.html', context)


def detail_athlete(request, id, slug):
    athlete = Athlete.objects.select_related(
        'stream', 'team__stream', 'club', 'squad'
    ).get(id=id)

    disciplines = athlete.stream.get_ordered_disciplines()

    athletes_disciplines_result_dict = athlete.stream.get_athletes_disciplines_result_dict()
    athletes_disciplines_rank_dict = athlete.stream.get_athletes_disciplines_rank_dict(athletes_disciplines_result_dict)

    context = {
        'athlete': athlete,
        'disciplines': disciplines,
        'athlete_disciplines_result_dict': athletes_disciplines_result_dict[athlete.id],
        'athlete_disciplines_rank_dict': athletes_disciplines_rank_dict[athlete.id] }
    return render(request, 'gymnastics/athletes/detail.html', context)


def results(request):
    context = { 'athletes': Athlete.objects.all() }
    return render(request, 'gymnastics/athletes/results.html', context)


class AthleteCreateView(generic.CreateView):

    model = Athlete
    fields = ['first_name', 'last_name', 'sex', 'date_of_birth', 'stream', 'club', 'team', 'squad']
    template_name = 'gymnastics/athletes/new.html'


class AthleteUpdateView(generic.UpdateView):

    model = Athlete
    fields = ['first_name', 'last_name', 'sex', 'date_of_birth', 'stream', 'club', 'team', 'squad']
    template_name = 'gymnastics/athletes/edit.html'

    # context_object_name = 'athlete' # should be available as well as object because of model = Athlete
    # form_class = AthleteForm

    # def get_success_url(self):
    #     return reverse('athletes.detail', kwargs = { 'id' : self.kwargs['pk'] })

    # def get_context_data(self, **kwargs):
    #     context = super(AthleteUpdateView, self).get_context_data(**kwargs)
    #     context['latest_articles'] = Article.objects.all()[:5]
    #     return context

    # def form_invalid(self, form):
    #     if form.non_field_errors():
    #         error_message = "The provided combination of fields is not accepted and thus the object can't be saved."
    #         messages.error(self.request, error_message)

    #     # TODO: check 'striptags' django template tag to easily render generated errors from ModelForms

    #     # TODO: give more details about those errors from the ErrorLists
    #     # ErrorLists: (field.errors['field_name']) and field.non_field_errors
    #     if form.errors:
    #         error_fields_labels = [form[field_with_error].label for field_with_error in form.errors]
    #         error_message_base = 'There are errors in the following fields:'
    #         error_fields_message = ', '.join(error_fields_labels)
    #         error_message = '{0} {1}'.format(error_message_base, error_fields_message)
    #         messages.error(self.request, error_message)

    #     return super().form_invalid(form)

    # def get(self, request, *args, **kwargs):
    #     view = AthleteUpdateView.as_view()
    #     return view(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     view = AthleteUpdateView.as_view()
    #     return view(request, *args, **kwargs)


class AthleteDeleteView(generic.DeleteView):

    model = Athlete
    template_name = 'gymnastics/athletes/delete.html'
    success_url = reverse_lazy('athletes.index')

    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super().dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = { "result": "ok" }
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp



# Just here as reference as we probably need it for bulk creation of athletes
# class AthleteForm(ModelForm):
#     class Meta:
#         model = Athlete
#         fields = ['first_name', 'last_name', 'sex', 'year_of_birth', 'club', 'squad', 'stream', 'team']
#         # widgets = {
#         #     name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
#         # }


# # plain update controller logic. keep for bulk-insert!!!
# def edit(request, pk):
#     if request.method == 'GET':
#         try:
#             context = {'athlete': Athlete.objects.get(id=pk)}
#         except:
#             # TODO
#             print('!!!!!!!!!!!!!!!!!!!!!!')
#             pass

#         # print(context)
#         # print(context['athlete'])
#         # print(dir(context['athlete']))
#         # print(Athlete)
#         # print(dir(Athlete))

#         return render(request, 'gymnastics/athletes/edit.html', context)
#     elif request.method == 'POST':
#         # print(request.POST)
#         # print(type(request.POST))

#         # verify all request.POST fields in athlete and set them if they changed
#         # OR
#         # set all athlete fields to the corresponding request.POST values
#         # then try saving it
#         # use verifier on the athlete model to raise proper exceptions if values are shit
#         # catch these exceptions here (maybe use custom clasa)
#         # put error messages together and render them

#         athlete = Athlete.objects.get(id=pk)

#         # assign all request.POST values to the corresponding athlete field
#         for key, value in request.POST.items():
#             if hasattr(athlete, key):
#                 setattr(athlete, key, value)

#         # validate athlete - calls clean_fields, clean and validate_unique
#         # athlete.full_clean()

#         #simple test
#         # athlete.first_name = request.POST['first_name']

#         try:
#             athlete.save()
#             # render success
#         except Exception as e:
#             # set error messages (eine error message mit allen exceptions or vice versa)
#             # add errors to context
#             return render(request, 'gymnastics/athletes/edit2.html', context)

#         # render success
#         context = {'object': athlete}
#         return render(request, 'gymnastics/athletes/detail.html', context)

#     #http 405! 404?
#     return  HttpResponseNotAllowed(['GET', 'POST'])
#     # ToDO: add 405.http basic template
#     # return  HttpResponseNotAllowed(['PUT'])


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

    if(len(elements) > 6 and elements[3] == ''):
        elements = elements[:3] + elements[4:]

    if(len(elements) > 6 and elements[1] == ''):
        elements = elements[:1] + elements[2:]

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

    stream_name = elements[3]
    try:
        stream = Stream.objects.get(difficulty=stream_name, sex=sex)
        if date_of_birth.year < stream.minimum_year_of_birth:
            return None
    except:
        return None

    athlete = Athlete( \
            first_name=elements[0],
            last_name=elements[1],
            sex=sex,
            date_of_birth=date_of_birth,
            club=club,
            stream=stream,
            athletes_import=athletes_import)

    team_name = elements[4]

    if team_name:
        try:
            team = club.team_set.get(stream=stream, name=team_name)
        except:
            team = Team(club=club, stream=stream, name=team_name)
            team.save()
        if team and team.athlete_set.count() < stream.all_around_team_size:
            athlete.team = team
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
