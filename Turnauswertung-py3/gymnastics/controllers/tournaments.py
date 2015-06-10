import json

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy
from django.shortcuts import redirect, render
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
    template_location = 'gymnastics/pdfs/certificates.tex'
    file_name = 'filename={0}.pdf'.format(ugettext_lazy('Certificates'))

    return pdf.create(template_location, context, file_name)

def create_evaluation_pdf(request, id, slug):

    streams = Stream.objects.all() \
        .prefetch_related('discipline_set') \
        .prefetch_related('athlete_set') \
        .prefetch_related('team_set__athlete_set__performance_set') \
        .order_by('sex', '-minimum_year_of_birth', 'difficulty')

    clubs = Club.objects.all() \
        .prefetch_related('athlete_set')
    
    athlete_disciplines_rank_dict = {}
    athlete_disciplines_result_dict = {}
    club_stream_athlete_number_dict = {}
    stream_athletes_dict = {}
    stream_disciplines_dict = {}
    stream_teams_dict = {}
    team_athletes_dict = {}
    team_disciplines_rank_dict = {}
    team_disciplines_result_dict = {}

    stream_athletes_disciplines_rank_dict = {}
    stream_athletes_disciplines_result_dict = {}
    stream_teams_disciplines_result_dict = {}
    stream_teams_disciplines_rank_dict = {}
    


    # dict1.update(dict2)
    # dict1.pop(key[, default])
    for stream in streams:
        stream_disciplines_dict[stream.id] = stream.get_ordered_disciplines()

        stream_athletes_dict[stream.id] = stream.athlete_set.all() \
            .select_related('club').select_related('stream').select_related('team__stream').select_related('squad') \
            .prefetch_related('performance_set')

        stream_athletes_disciplines_result_dict[stream.id] = stream_athletes_dict.get(stream.id).get_athletes_disciplines_result_dict()
        stream_athletes_disciplines_rank_dict[stream.id] = stream.get_athletes_disciplines_rank_dict(stream_athletes_disciplines_result_dict.get(stream.id, {}))

        stream_teams_dict[stream.id] = stream.team_set.all() \
            .select_related('stream').select_related('club') \
            .prefetch_related('athlete_set')

        stream_teams_disciplines_result_dict[stream.id] = stream.get_teams_disciplines_result_dict()
        stream_teams_disciplines_rank_dict[stream.id] = stream.get_teams_disciplines_rank_dict(stream_teams_disciplines_result_dict.get(stream.id, {}))

        stream_athletes_dict[stream.id] = [athlete for athlete in stream_athletes_dict[stream.id] if stream_athletes_disciplines_result_dict.get(stream.id).get(athlete.id).get('total', 0.0) > 0.0]
        stream_teams_dict[stream.id] = [team for team in stream_teams_dict[stream.id] if stream_teams_disciplines_result_dict.get(stream.id).get(team.id).get('total', 0.0) > 0.0]

        stream_athletes_dict[stream.id] = sorted(stream_athletes_dict.get(stream.id), key=lambda athlete: stream_athletes_disciplines_rank_dict.get(stream.id).get(athlete.id).get('total'))
        stream_teams_dict[stream.id] = sorted(stream_teams_dict.get(stream.id), key=lambda team: stream_teams_disciplines_rank_dict.get(stream.id).get(team.id).get('total'))

        athlete_disciplines_rank_dict.update(stream_athletes_disciplines_rank_dict[stream.id])
        athlete_disciplines_result_dict.update(stream_athletes_disciplines_result_dict[stream.id])
        team_disciplines_rank_dict.update(stream_teams_disciplines_rank_dict[stream.id])
        team_disciplines_result_dict.update(stream_teams_disciplines_result_dict[stream.id])

        team_athletes_dict.update({team.id: [athlete for athlete in team.athlete_set.all() if stream_athletes_disciplines_result_dict.get(stream.id).get(athlete.id).get('total') > 0.0] for team in stream_teams_dict[stream.id]})

    streams = [stream for stream in streams if len(stream_athletes_dict.get(stream.id, [])) > 0]

    club_stream_athlete_number_dict = { 
        club.id: 
            {stream.id: len(set(stream_athletes_dict.get(stream.id, [])) & set(club.athlete_set.all()))
                for stream in streams}
        for club in clubs}

    for club in clubs:
        club_stream_athlete_number_dict[club.id]['total'] = sum(club_stream_athlete_number_dict.get(club.id, {}).values())

    statistics_format_dict = {
        'start': len(streams),
        'end': len(streams)+1,
        'female_number': len([stream for stream in streams if stream.sex == 'f']),
        'male_number': len([stream for stream in streams if stream.sex == 'm'])
    }

    context = {
        'clubs': clubs,
        'club_stream_athlete_number_dict': club_stream_athlete_number_dict,
        'statistics_format_dict': statistics_format_dict,
        'streams': streams,
        'stream_athletes_dict': stream_athletes_dict,
        'athlete_disciplines_rank_dict': athlete_disciplines_rank_dict,
        'athlete_disciplines_result_dict': athlete_disciplines_result_dict,
        'stream_disciplines_dict': stream_disciplines_dict,
        'stream_teams_dict': stream_teams_dict,
        'team_disciplines_rank_dict': team_disciplines_rank_dict,
        'team_disciplines_result_dict': team_disciplines_result_dict,
        'team_athletes_dict': team_athletes_dict,
        'total_athletes': sum([len(athlete_list) for athlete_list in stream_athletes_dict.values()]),
        'tournament': Tournament.objects.get(id=id)
    }
    template_location = 'gymnastics/pdfs/evaluation.tex'
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