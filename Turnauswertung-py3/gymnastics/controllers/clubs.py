from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from gymnastics.models.club import Club


def index(request):
    context = { 'clubs': Club.objects.all() }
    return render(request, 'gymnastics/clubs/index.html', context)

def detail(request, id):
    context = { 'club': Club.objects.get(id=id) }
    return render(request, 'gymnastics/clubs/detail.html', context)


class ClubCreateView(generic.CreateView):

    model = Club
    fields = ['name']
    template_name = 'gymnastics/clubs/new.html'
    success_url = reverse_lazy('clubs.index')


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
