from django.core.urlresolvers import reverse
from django.db import models

from gymnastics.models.stream import Stream

class Team(models.Model):
  
    name = models.CharField(max_length=50, null=False)

    club = models.ForeignKey('Club', null=True, blank=True)
    stream = models.ForeignKey('Stream')

    class Meta:
        db_table = 'gymnastics_teams'    

    def __str__(self):
        return "{0} ({1})".format(self.name, self.stream)

    # discipline.id -> performance_value
    @property
    def disciplines_result_dict(self):
        # list with all team performances
        athletes_performances_dicts = (athlete.performances_dict for athlete in self.athlete_set.all())

        # sum via sorted



    # discipline -> performance_value
    def discipline_performance(self):
        performance_dict = {}
        for athlete in self.athlete_set.all():
            for discipline, value in athlete.performances().items():
                if not performance_dict.get(discipline):
                    performance_dict[discipline] = []
                performance_dict[discipline].append(value)

        for discipline, performance_list in performance_dict.items():
            performance_dict[discipline] = sum(sorted(performance_list, reverse=True)[:self.stream.all_around_team_counting_athletes])

        return performance_dict

    @property
    def all_around_total(self):
        return sum(self.discipline_performance().values())
