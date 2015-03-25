from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.views import generic

from gymnastics.models.club import Club


def index(request):
    context = { 'clubs': Club.objects.all() \
        .prefetch_related('athlete_set') }
    return render(request, 'gymnastics/clubs/index.html', context)

def detail(request, id):
    # Club
    club = Club.objects.select_related().get(id=id)

    # Athletes: stream.athlete_set
    athletes = club.athlete_set.all() \
        .select_related('club').select_related('stream').select_related('team').select_related('squad')

    context = { 
        'club': club, 
        'athletes': athletes,
    }
    return render(request, 'gymnastics/clubs/detail.html', context)


class ClubCreateView(SuccessMessageMixin, generic.CreateView):

    model = Club
    fields = ['name']
    template_name = 'gymnastics/clubs/new.html'
    success_url = reverse_lazy('clubs.index')
    success_message = "%(name)s was created successfully"


class ClubUpdateView(generic.UpdateView):

    model = Club
    fields = ['name']
    template_name = 'gymnastics/clubs/edit.html'

    def get_success_url(self):
        some_kwargs = self.kwargs
        return reverse('clubs.detail', kwargs = { 'pk' : self.kwargs['pk'] })


class ClubDeleteView(generic.DeleteView):

    model = Club
    template_name = 'gymnastics/clubs/delete.html'
    success_url = reverse_lazy('clubs.index')
