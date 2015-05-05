import json

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse, reverse_lazy
# from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views import generic

from gymnastics.models import Athlete, AthletesImport, Club, Stream, Team


def index(request):
    context = { 
        'athletes': Athlete.objects.all() \
            .select_related('club').select_related('stream').select_related('team__stream').select_related('squad') 
    }
    return render(request, 'gymnastics/athletes/index.html', context)

def detail(request, id):
    athlete = Athlete.objects \
        .select_related('stream') \
            .prefetch_related('stream__discipline_set') \
            .prefetch_related('stream__athlete_set') \
                .prefetch_related('stream__athlete_set__performance_set') \
        .select_related('team') \
        .select_related('club') \
        .select_related('squad') \
        .get(id=id)

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


class AthleteCreateView(SuccessMessageMixin, generic.CreateView):

    model = Athlete
    fields = ['first_name', 'last_name', 'sex', 'year_of_birth', 'date_of_birth', 'club', 'squad', 'stream', 'team']
    template_name = 'gymnastics/athletes/new.html'
    success_url = reverse_lazy('athletes.index')
    success_message = "%(first_name)s %(last_name)s was created successfully"


class AthleteUpdateView(SuccessMessageMixin, generic.UpdateView):

    model = Athlete
    fields = ['first_name', 'last_name', 'sex', 'year_of_birth', 'date_of_birth', 'club', 'squad', 'stream', 'team']
    template_name = 'gymnastics/athletes/edit.html'
    success_message = "%(first_name)s %(last_name)s was edited successfully"

    # context_object_name = 'athlete' # should be available as well as object because of model = Athlete
    # form_class = AthleteForm

    def get_success_url(self):
        return reverse('athletes.detail', kwargs = { 'id' : self.kwargs['pk'] })

    # def get_context_data(self, **kwargs):
    #     context = super(AthleteUpdateView, self).get_context_data(**kwargs)
    #     context['latest_articles'] = Article.objects.all()[:5]
    #     return context

    def form_invalid(self, form):
        if form.non_field_errors():
            error_message = "The provided combination of fields is not accepted and thus the object can't be saved."
            messages.error(self.request, error_message)

        # TODO: check 'striptags' django template tag to easily render generated errors from ModelForms

        # TODO: give more details about those errors from the ErrorLists 
        # ErrorLists: (field.errors['field_name']) and field.non_field_errors
        if form.errors:
            error_fields_labels = [form[field_with_error].label for field_with_error in form.errors]
            error_message_base = 'There are errors in the following fields:'
            error_fields_message = ', '.join(error_fields_labels)
            error_message = '{0} {1}'.format(error_message_base, error_fields_message)
            messages.error(self.request, error_message)

        return super().form_invalid(form)

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
            response_data = {"result": "ok"}
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