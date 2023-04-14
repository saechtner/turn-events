import operator

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy


class Stream(models.Model):

    difficulty = models.CharField(
        gettext_lazy('Difficulty'), max_length=10, null=False)
    sex = models.CharField(gettext_lazy('Sex'), max_length=1, null=False, choices=(('m', gettext_lazy('male')), ('f', gettext_lazy('female'))), default='f')
    minimum_year_of_birth = models.IntegerField(
        gettext_lazy('Minimum Year of Birth'), default=2000, null=False)

    all_around_individual = models.BooleanField(
        gettext_lazy('All around individual'), default=True)
    all_around_individual_counting_events = models.IntegerField(
        null=True, blank=True, default=4)

    all_around_team = models.BooleanField(
        gettext_lazy('All around team'), default=True)
    all_around_team_size = models.IntegerField(
        null=True, blank=True, default=4)
    all_around_team_counting_athletes = models.IntegerField(
        null=True, blank=True, default=4)

    discipline_finals = models.BooleanField(
        gettext_lazy('Discipline finals'), default=False)
    discipline_finals_max_participants = models.IntegerField(
        null=True, blank=True)
    discipline_finals_both_values_count = models.BooleanField(
        blank=True, default=True)

    discipline_set = models.ManyToManyField(
        'common.Discipline', through='common.StreamDisciplineJoin')

    slug = models.SlugField(max_length=127, blank=True)

    class Meta:
        app_label = "streams"

    def __str__(self):
        return "{0} {1}".format(self.difficulty, self.get_sex_display())

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = str(slugify(str(self)))
        return super(Stream, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'streams.detail', kwargs={'id': self.id, 'slug': self.slug})

    def get_edit_url(self):
        return reverse(
            'streams.edit', kwargs={'id': self.id, 'slug': self.slug})

    def get_delete_url(self):
        return reverse(
            'streams.delete', kwargs={'pk': self.id, 'slug': self.slug})

    def get_ordered_disciplines(self):
        return self.discipline_set.order_by('streamdisciplinejoin__position')

    def get_athletes_disciplines_result_dict(self, athletes=None):
        if not athletes:
            athletes = self.athlete_set.prefetch_related(
                'performance_set'
            ).all()
        return athletes.get_athletes_disciplines_result_dict()

    def get_athletes_disciplines_rank_dict(self, athletes_disciplines_result_dict=None):
        if athletes_disciplines_result_dict is None:
            athletes_disciplines_result_dict = self.get_athletes_disciplines_result_dict()
        return self._rank_results(self.athlete_set.all(), athletes_disciplines_result_dict)

    def get_teams_disciplines_result_dict(self):
        teams_disciplines_result_dict = {}
        for team in self.team_set.all():
            team_dict = team.get_disciplines_result_dict()
            teams_disciplines_result_dict[team.id] = team_dict
            teams_disciplines_result_dict[team.id]['total'] = team.get_all_around_result(team_dict)
        return teams_disciplines_result_dict

    def get_teams_disciplines_rank_dict(self, teams_disciplines_result_dict=None):
        if teams_disciplines_result_dict is None:
            teams_disciplines_result_dict = self.get_teams_disciplines_result_dict()
        return self._rank_results(self.team_set.all(), teams_disciplines_result_dict)

    def _rank_results(self, model_objects, disciplines_result_dict):
        disciplines_rank_dict = { o.id: {} for o in model_objects }

        discipline_keys = [disc.id for disc in self.discipline_set.all()]
        discipline_keys.append('total')

        for disc_key in discipline_keys:
            performances_pre_sort = ((key, value.get(disc_key, 0)) for key, value in disciplines_result_dict.items())
            performances_sorted = sorted(performances_pre_sort, key=operator.itemgetter(1), reverse=True)
            prev_value = None
            equal_value_counter = 0
            for rank, id_value_tuple in enumerate(performances_sorted, start=1):
                equal_value_counter = equal_value_counter + 1 if prev_value == id_value_tuple[1] else 0
                disciplines_rank_dict[id_value_tuple[0]][disc_key] = rank - equal_value_counter
                prev_value = id_value_tuple[1]

        return disciplines_rank_dict

    # TODO:: rework / remove!
    def final_rank(self):
        participants = self.final_participants()
        discipline_rank_dict = {}
        for discipline in self.discipline_set.all():
            athlete_list = sorted({athlete: athlete.final_total(discipline) \
                for athlete in participants.get(discipline)}.items(), key=lambda x: x[1], reverse=True)
            rank = 1
            prevTotal = athlete_list[0][1]
            ranks_dict = {}
            for athlete, total_value in athlete_list:
                if total_value < prevTotal:
                    rank += 1
                ranks_dict[athlete] = rank
            discipline_rank_dict[discipline] = ranks_dict
        return discipline_rank_dict

    # TODO:: rework / remove!
    def final_participants(self):
        participants_dict = {}
        for discipline in self.discipline_set.all():
            discipline_performances = {}
            for athlete in self.athlete_set.all():
                athlete_performance = athlete.performances()[discipline]
                if not discipline_performances.get(athlete_performance):
                    discipline_performances[athlete_performance] = []
                discipline_performances[athlete_performance].append(athlete)
            participants_dict[discipline] = []
            for value, athlete_list in sorted(discipline_performances.items(), reverse=True):
                participants_dict[discipline].extend(athlete_list)
                if len(participants_dict[discipline]) >= self.discipline_finals_max_participants:
                    break
        return participants_dict
