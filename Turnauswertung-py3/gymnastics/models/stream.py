import operator

from django.db import models
from django.utils.translation import ugettext_lazy as _

from gymnastics.models.discipline import Discipline
from gymnastics.models.stream_discipline_join import StreamDisciplineJoin

class Stream(models.Model):
  
    difficulty = models.CharField(max_length=10, null=False)
    sex = models.CharField(max_length=1, null=False, choices=(('m', _('male')), ('f', _('female'))), default='f')
    minimum_year_of_birth = models.IntegerField(default=2000, null=False, verbose_name='minimum Year of Birth')
    
    all_around_individual = models.BooleanField(default=True)
    all_around_individual_counting_events = models.IntegerField(null=True, blank=True, default=4)
    all_around_team = models.BooleanField(default=True)
    all_around_team_counting_athletes = models.IntegerField(null=True, blank=True, default=4)
    discipline_finals = models.BooleanField(default=False)
    discipline_finals_max_participants = models.IntegerField(null=True, blank=True)
    discipline_finals_both_values_count = models.BooleanField(blank=True, default=True)

    discipline_set = models.ManyToManyField('Discipline', through='StreamDisciplineJoin')

    class Meta:
        db_table = 'gymnastics_streams'
        
    def __str__(self):
        return "{0} {1}".format(self.difficulty, self.get_sex_display())

    def get_athletes_disciplines_result_dict(self):
        athletes_disciplines_result_dict = { a.id: a.get_disciplines_result_dict() for a in self.athlete_set.all() }

        for athlete in self.athlete_set.all():
            athletes_disciplines_result_dict[athlete.id]['total'] = athlete.get_all_around_result()

        return athletes_disciplines_result_dict

    def get_athletes_disciplines_rank_dict(self, athletes_disciplines_result_dict=None):
        if not athletes_disciplines_result_dict:
            athletes_disciplines_result_dict = self.get_athletes_disciplines_result_dict()
        return self._rank_results(self.athlete_set.all(), athletes_disciplines_result_dict)

    def get_teams_disciplines_result_dict(self):
        teams_disciplines_result_dict = { t.id: t.get_disciplines_result_dict() for t in self.team_set.all() }

        for team in self.team_set.all():
            teams_disciplines_result_dict[team.id]['total'] = team.get_all_around_result(teams_disciplines_result_dict[team.id])

        return teams_disciplines_result_dict

    def get_teams_disciplines_rank_dict(self, teams_disciplines_result_dict=None):
        if not teams_disciplines_result_dict:
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