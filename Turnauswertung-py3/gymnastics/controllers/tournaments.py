import json

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views import generic

from gymnastics.models import Club, Tournament


def index(request):
    context = { 'tournaments': Tournament.objects.all().select_related('club')}
    return render(request, 'gymnastics/tournaments/index.html', context)

def detail(request, id):
    tournament = Tournament.objects.get(id=id)
    context = {'tournament': tournament}
    return render(request, 'gymnastics/tournaments/detail.html', context)

class TournamentCreateView(SuccessMessageMixin, generic.CreateView):

    model = Tournament
    fields = ['name', 'date', 'location', 'club']
    template_name = 'gymnastics/tournaments/new.html'
    success_url = reverse_lazy('tournaments.index')
    success_message = "%(name)s was created successfully"


class TournamentUpdateView(SuccessMessageMixin, generic.UpdateView):

    model = Tournament
    fields = ['name', 'date', 'location', 'club']
    template_name = 'gymnastics/tournaments/edit.html'
    success_message = "%(name)s was edited successfully"

    def get_success_url(self):
        return reverse('tournaments.detail', kwargs = { 'id' : self.kwargs['pk'] })

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

class TournamentDeleteView(generic.DeleteView):

    model = Tournament
    template_name = 'gymnastics/tournaments/delete.html'
    success_url = reverse_lazy('tournaments.index')

    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super().dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp