import json

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader, Context
from django.utils.translation import ugettext_lazy
from django.views import generic

from gymnastics.models import Club, Tournament, Stream
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
    template_location = 'gymnastics/documents/certificates.tex'
    file_name = 'filename={0}.pdf'.format(ugettext_lazy('Certificates'))

    return pdf.create(template_location, context, file_name)

def create_solo_data_txt(request, id, slug):
    response = HttpResponse(content_type='text')
    response['Content-Disposition'] = 'attachment; filename="{0}.txt"'.format(ugettext_lazy('solo_data'))

    data = Tournament.objects.get(id=id).get_evaluation_data()

    context = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(ugettext_lazy('Club'), ugettext_lazy('Total'), ugettext_lazy('Rank'), ugettext_lazy('Stream'), ugettext_lazy('Last Name'), ugettext_lazy('First Name'))
    for stream in data.get('streams'):
        for athlete in data.get('stream_athletes_dict').get(stream.id)[:3]:
            first_name = athlete.first_name
            last_name = athlete.last_name
            club = str(athlete.club)
            stream = str(stream)
            total = str(data.get('athlete_disciplines_result_dict').get(athlete.id).get('total'))
            rank = str(data.get('athlete_disciplines_rank_dict').get(athlete.id).get('total'))

            athlete_line = "\t".join([club, total, rank, stream, last_name, first_name])
            context = "\n".join([context, athlete_line])

    response.write(context)
    return response

def create_team_data_txt(request, id, slug):
    response = HttpResponse(content_type='text')
    response['Content-Disposition'] = 'attachment; filename="{0}.txt"'.format(ugettext_lazy('team_data'))

    data = Tournament.objects.get(id=id).get_evaluation_data()

    context = "{0}\t{1}\t{2}\t{3}\t{4}".format(ugettext_lazy('Team'), ugettext_lazy('Total'), ugettext_lazy('Rank'), ugettext_lazy('Stream'), ugettext_lazy('Athletes'))
    for stream in data.get('streams'):
        for team in data.get('stream_teams_dict').get(stream.id)[:2]:
            stream = str(stream)
            total = str(data.get('team_disciplines_result_dict').get(team.id).get('total'))
            rank = str(data.get('team_disciplines_rank_dict').get(team.id).get('total'))
            athletes = ','.join([str(athlete) for athlete in data.get('team_athletes_dict').get(team.id)])

            team_line = "\t".join([str(team), total, rank, stream, athletes])
            context = "\n".join([context, team_line])

    response.write(context)
    return response

def create_evaluation_pdf(request, id, slug):

    context = Tournament.objects.get(id=id).get_evaluation_data()

    clubs = Club.objects.all().prefetch_related('athlete_set')
    streams = context.get('streams')
    stream_athletes_dict = context.get('stream_athletes_dict')
    stream_teams_dict = context.get('stream_teams_dict')
    team_athletes_dict = context.get('team_athletes_dict')
    
    teams = sum(stream_teams_dict.values(), [])
    team_format_dict = {team.id: -(len(team_athletes_dict[team.id]) + 1) for team in teams}

    club_stream_athlete_number_dict = { 
        club.id: 
            {stream.id: len(set(stream_athletes_dict.get(stream.id, [])) & set(club.athlete_set.all()))
                for stream in streams}
        for club in clubs}

    # make pythonic
    for club in clubs:
        club_stream_athlete_number_dict[club.id]['total'] = sum(club_stream_athlete_number_dict.get(club.id, {}).values())

    clubs = [club for club in clubs if club_stream_athlete_number_dict[club.id].get('total', 0) > 0]

    statistics_format_dict = {
        'start': len(streams),
        'end': len(streams) + 1,
        'female_number': len([stream for stream in streams if stream.sex == 'f']),
        'male_number': len([stream for stream in streams if stream.sex == 'm'])
    }

    context['club_stream_athlete_number_dict'] = club_stream_athlete_number_dict
    context['clubs'] = clubs
    context['statistics_format_dict'] = statistics_format_dict
    context['team_format_dict'] = team_format_dict
    context['total_athletes'] = sum([len(athlete_list) for athlete_list in stream_athletes_dict.values()])

    template_location = 'gymnastics/documents/evaluation.tex'
    file_name = '{0}.pdf'.format(ugettext_lazy('Evaluation'))

    return pdf.create(template_location, context, file_name)



class TournamentCreateView(generic.CreateView):

    model = Tournament
    fields = ['name', 'name_full', 'date', 'hosting_club', 'address', 'region', 'management', 'organisation', 'calculation', 'technology']
    template_name = 'gymnastics/tournaments/new.html'


class TournamentUpdateView(generic.UpdateView):

    model = Tournament
    fields = ['name', 'name_full', 'date', 'hosting_club', 'address', 'region', 'management', 'organisation', 'calculation', 'technology']
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