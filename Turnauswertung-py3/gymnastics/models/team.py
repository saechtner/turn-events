from django.core.urlresolvers import reverse
from django.db import models


class Team(models.Model):
  
    name = models.CharField(max_length=50, null=False)

    club = models.ForeignKey('Club', null=True, blank=True)
    stream = models.ForeignKey('Stream')

    class Meta:
        db_table = 'gymnastics_teams'    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teams.detail', kwargs={ 'id': self.id })

    def get_edit_url(self):
        return reverse('teams.edit', kwargs={ 'pk': self.id })

    def get_delete_url(self):
        return reverse('teams.delete', kwargs={ 'pk': self.id })

    def get_disciplines_result_dict(self):
        disciplines_results_dict = { disc.id: [] for disc in self.stream.discipline_set.all() }
        for athlete in self.athlete_set.all():
            for perf in athlete.performance_set.all():
                disciplines_results_dict[perf.discipline_id].append(perf.value)

        counting_athletes = self.stream.all_around_team_counting_athletes
        return { k: sum(sorted(v, reverse=True)[:counting_athletes]) for k, v in disciplines_results_dict.items() }

    def get_all_around_result(self, disciplines_result_dict=None):
        if not disciplines_result_dict:
            disciplines_result_dict = self.get_disciplines_result_dict()
        return sum(disciplines_result_dict.values())
