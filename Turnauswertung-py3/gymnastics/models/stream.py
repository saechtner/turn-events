from django.db import models

from gymnastics.models.discipline import Discipline

class Stream(models.Model):
  
    difficulty = models.CharField(max_length=10, null=False)
    sex = models.CharField(max_length=1, null=False, choices=(('m', 'male'), ('f', 'female')), default='f')
    minimum_year_of_birth = models.IntegerField(default=2000, null=False)
    all_around_individual = models.BooleanField(default=True)
    all_around_individual_counting_events = models.IntegerField(null=True, blank=True, default=4)
    all_around_team = models.BooleanField(default=True)
    all_around_team_counting_athletes = models.IntegerField(null=True, blank=True, default=4)
    discipline_finals = models.BooleanField(default=False)
    discipline_finals_max_participants = models.IntegerField(null=True, blank=True)

    discipline_set = models.ManyToManyField('Discipline')


    class Meta:
        db_table = 'gymnastics_streams'
        
    def __str__(self):
        return "{0} {1}".format(self.difficulty, self.get_sex_display())