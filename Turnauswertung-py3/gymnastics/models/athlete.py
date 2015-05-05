from django.db import models


class Athlete(models.Model):
  
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    sex = models.CharField(max_length=1, null=False, choices=(('m', 'male'), ('f', 'female')), default='f')
    year_of_birth = models.IntegerField(default=2000) # deprecated. Gonna get removed soonish
    date_of_birth = models.DateField(default='1900-01-01')

    club = models.ForeignKey('Club', null=True, blank=True)
    stream = models.ForeignKey('Stream')
    team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL)
    squad = models.ForeignKey('Squad', null=True, blank=True, on_delete=models.SET_NULL)

    athletes_import = models.ForeignKey('AthletesImport', null=True, blank=True)


    class Meta:
        db_table = 'gymnastics_athletes'

    def __str__(self):
        # Dev Output
        # return 'Athlete: [name: {0} {1}, sex: {2}, year_of_birth: {3}, club; {4}, stream: {5}]'.format( \
        #     self.first_name, self.last_name, self.sex, self.year_of_birth, self.club, self.stream)
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_disciplines_result_dict(self):
        return { perf.discipline_id: perf.value for perf in self.performance_set.all() }

    def get_all_around_result(self):
        results_sorted = sorted((perf.value for perf in self.performance_set.all()), reverse=True)
        return sum(results_sorted[:self.stream.all_around_individual_counting_events])


    # TODO:: rework!
    def final_total(self, discipline):
        total = 0
        if self.stream.discipline_finals_both_values_count:
            total += self.performances().get(discipline)
        x = self.performances_final().get(discipline)
        if x != None:
            total += x
        return total
