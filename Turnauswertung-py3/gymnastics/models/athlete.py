from django.db import models
from django.db.models import Sum


class Athlete(models.Model):
  
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    sex = models.CharField(max_length=1, null=False, choices=(('m', 'male'), ('f', 'female')), default='f')
    year_of_birth = models.IntegerField(default=2000)

    club = models.ForeignKey('Club', null=True, blank=True)
    squad = models.ForeignKey('Squad', null=True, blank=True)
    stream = models.ForeignKey('Stream', null=False)
    team = models.ForeignKey('Team', null=True, blank=True)


    class Meta:
        db_table = 'gymnastics_athletes'

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def performance_total(self):
        return self.performance_set \
            .order_by("value")[:self.stream.all_around_individual_counting_events] \
            .aggregate(Sum('value')).get('value__sum', 0.00)

    def performances(self):
        return {performance.discipline: performance.value for performance in self.performance_set.all()}

    def performances_final(self):
        return {performance.discipline: performance.value_final for performance in self.performance_set.all()}

    def final_total(self, discipline):
        total = self.performances().get(discipline)
        x = self.performances_final().get(discipline)
        if x != None:
            total += x
        return total