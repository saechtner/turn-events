import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy

from streams.models import Stream


class Tournament(models.Model):

    name = models.CharField(
        ugettext_lazy('Name'), max_length=50, default='KJSS 2015')
    name_full = models.CharField(ugettext_lazy('Full Name'), max_length=255)
    date = models.DateField(ugettext_lazy('Date'), default=datetime.date.today)
    region = models.CharField(
        ugettext_lazy('Region'), max_length=128, null=True, blank=True)

    management = models.CharField(
        ugettext_lazy('Management'), max_length=128, null=True, blank=True)
    organisation = models.CharField(
        ugettext_lazy('Organisation'), max_length=128, null=True, blank=True)
    calculation = models.CharField(
        ugettext_lazy('Calculation'), max_length=128, null=True, blank=True)
    technology = models.CharField(
        ugettext_lazy('Technology'), max_length=128, null=True, blank=True)

    address = models.ForeignKey(
        'common.Address', null=True, blank=True, on_delete=models.CASCADE,
        verbose_name=ugettext_lazy('Address')
    )
    hosting_club = models.ForeignKey(
        'clubs.Club', null=True, blank=True, on_delete=models.CASCADE,
        verbose_name=ugettext_lazy('Hosting club')
    )

    slug = models.SlugField(max_length=128, blank=True)

    class Meta:
        app_label = "tournaments"

    def __str__(self):
        return '{0}'.format(self.name)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = str(slugify(str(self)))
        return super(Tournament, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tournaments.detail', kwargs={ 'id': self.id, 'slug': self.slug })

    def get_delete_url(self):
        return reverse('tournaments.delete', kwargs={ 'pk': self.id, 'slug': self.slug })

    def get_edit_url(self):
        return reverse('tournaments.edit', kwargs={ 'pk': self.id, 'slug': self.slug })

    def get_evaluation_url(self):
        return reverse('tournaments.create_evaluation_pdf', kwargs={ 'id': self.id, 'slug': self.slug })

    def get_solo_certificate_data_url(self):
        return reverse('tournaments.create_solo_certificate_data_txt', kwargs={ 'id': self.id, 'slug': self.slug })

    def get_team_certificate_data_url(self):
        return reverse('tournaments.create_team_certificate_data_txt', kwargs={ 'id': self.id, 'slug': self.slug })

    def get_evaluation_data(self):
        streams = (
            Stream.objects.all()
            .prefetch_related('discipline_set')
            .prefetch_related('athlete_set')
            .prefetch_related('athlete_set__club')
            .prefetch_related('athlete_set__stream')
            .prefetch_related('athlete_set__squad')
            .prefetch_related('athlete_set__team__stream')
            .prefetch_related('athlete_set__performance_set')
            .prefetch_related('athlete_set__performance_set__discipline')
            .prefetch_related('team_set')
            .prefetch_related('team_set__stream')
            .prefetch_related('team_set__club')
            .prefetch_related('team_set__stream')
            .prefetch_related('team_set__athlete_set')
            .prefetch_related('team_set__athlete_set__performance_set')
            .order_by('sex', '-minimum_year_of_birth', 'difficulty')
        )

        athlete_disciplines_rank_dict = {}
        athlete_disciplines_result_dict = {}
        stream_athletes_dict = {}
        stream_disciplines_dict = {}
        stream_teams_dict = {}
        team_athletes_dict = {}
        team_disciplines_rank_dict = {}
        team_disciplines_result_dict = {}

        for stream in streams:
            stream_disciplines_dict[stream.id] = stream.get_ordered_disciplines()

            stream_athletes_dict[stream.id] = stream.athlete_set.all() \
                .select_related('club').select_related('stream').select_related('team__stream').select_related('squad') \
                .prefetch_related('performance_set')

            stream_athletes_disciplines_result_dict = stream_athletes_dict.get(stream.id).get_athletes_disciplines_result_dict()
            stream_athletes_disciplines_rank_dict = stream.get_athletes_disciplines_rank_dict(stream_athletes_disciplines_result_dict)

            stream_teams_dict[stream.id] = stream.team_set.all() \
                .select_related('stream').select_related('club') \
                .prefetch_related('athlete_set')

            stream_teams_disciplines_result_dict = stream.get_teams_disciplines_result_dict()
            stream_teams_disciplines_rank_dict = stream.get_teams_disciplines_rank_dict(stream_teams_disciplines_result_dict)

            stream_athletes_dict[stream.id] = sorted(
                    [athlete for athlete in stream_athletes_dict[stream.id] if stream_athletes_disciplines_result_dict.get(athlete.id).get('total', 0.0) > 0.0],
                    key=lambda athlete: stream_athletes_disciplines_rank_dict.get(athlete.id).get('total')
                )
            stream_teams_dict[stream.id] = [team for team in stream_teams_dict[stream.id] if stream_teams_disciplines_result_dict.get(team.id).get('total', 0.0) > 0.0]

            team_athletes_dict.update({team.id: [athlete for athlete in team.athlete_set.all() if stream_athletes_disciplines_result_dict.get(athlete.id).get('total') > 0.0] for team in stream_teams_dict[stream.id]})
            stream_teams_dict[stream.id] = sorted(
                    [team for team in stream_teams_dict[stream.id] if stream.all_around_team_counting_athletes <= len(team_athletes_dict[team.id])],
                    key=lambda team: stream_teams_disciplines_rank_dict.get(team.id).get('total')
                )

            athlete_disciplines_rank_dict.update(stream_athletes_disciplines_rank_dict)
            athlete_disciplines_result_dict.update(stream_athletes_disciplines_result_dict)
            team_disciplines_rank_dict.update(stream_teams_disciplines_rank_dict)
            team_disciplines_result_dict.update(stream_teams_disciplines_result_dict)


        streams = [stream for stream in streams if len(stream_athletes_dict.get(stream.id, [])) > 0]

        context = {
            'athlete_disciplines_rank_dict': athlete_disciplines_rank_dict,
            'athlete_disciplines_result_dict': athlete_disciplines_result_dict,
            'host': self.hosting_club,
            'streams': streams,
            'stream_athletes_dict': stream_athletes_dict,
            'stream_disciplines_dict': stream_disciplines_dict,
            'stream_teams_dict': stream_teams_dict,
            'team_athletes_dict': team_athletes_dict,
            'team_disciplines_rank_dict': team_disciplines_rank_dict,
            'team_disciplines_result_dict': team_disciplines_result_dict,
            'tournament': self
        }

        return context

# TODO: add datepicker
# class MyForm(forms.Form):
#     date = forms.DateField(widget=AdminDateWidget)
