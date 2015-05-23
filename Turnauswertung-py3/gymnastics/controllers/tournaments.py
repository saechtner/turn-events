import json

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy
from django.shortcuts import redirect, render
from django.views import generic

from gymnastics.models import Club, Tournament
from gymnastics.utils import pdf


def index(request):
    context = { 'tournaments': Tournament.objects.all().select_related('club')}
    return render(request, 'gymnastics/tournaments/index.html', context)

def main(request):

    # TODO: find better solution to handle static constants such as this one
    main_tournament_name = 'KJSS 2015'
    
    try:
        tournament = Tournament.objects.filter(name=main_tournament_name)[0]
        return redirect(tournament.get_absolute_url())
    except:
        return redirect(reverse('tournaments.new'))

    return redirect(reverse('tournaments.index'))

def detail(request, id, slug):
    tournament = Tournament.objects.get(id=id)
    context = { 'tournament': tournament }
    return render(request, 'gymnastics/tournaments/detail.html', context)

def create_certificates_pdf(request):
    # squads = Squad.objects.all().prefetch_related('athlete_set').select_related('athlete_set__club')

    context = {
        'squads': [],
    }
    template_location = 'gymnastics/pdfs/certificates.tex'
    file_name = 'filename={0}.pdf'.format(ugettext_lazy('Certificates'))

    return pdf.create(template_location, context, file_name)


class TournamentCreateView(generic.CreateView):

    model = Tournament
    fields = ['name', 'name_full', 'date', 'address']
    template_name = 'gymnastics/tournaments/new.html'


class TournamentUpdateView(generic.UpdateView):

    model = Tournament
    fields = ['name', 'name_full', 'date', 'address']
    template_name = 'gymnastics/tournaments/edit.html'


class TournamentDeleteView(generic.DeleteView):

    model = Tournament
    template_name = 'gymnastics/tournaments/delete.html'
    success_url = reverse_lazy('tournaments.index')

    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super().dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = { "result": "ok" }
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp