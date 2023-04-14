from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy


class Team(models.Model):

    name = models.CharField(gettext_lazy('Name'), max_length=128, null=False)

    club = models.ForeignKey(
        'clubs.Club', null=True, blank=True, on_delete=models.CASCADE, verbose_name=gettext_lazy('Club')
    )
    stream = models.ForeignKey(
        'streams.Stream', on_delete=models.CASCADE, verbose_name=gettext_lazy('Stream'))

    class Meta:
        app_label = "teams"

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.stream)

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
