from django.db import models

from gymnastics.models.club import Club
from gymnastics.models.squad import Squad
from gymnastics.models.stream import Stream
from gymnastics.models.team import Team

class Athlete(models.Model):
  
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    sex = models.CharField(max_length=1, null=False, choices=(('m', 'male'), ('f', 'female')), default='f')
    year_of_birth = models.IntegerField(default=2000)

    club = models.ForeignKey(Club, null=True, blank=True)
    squad = models.ForeignKey(Squad, null=True, blank=True)
    stream = models.ForeignKey(Stream, null=False)
    team = models.ForeignKey(Team, null=True, blank=True)


    class Meta:
        db_table = 'gymnastics_athletes'

    def __str__(self):
        return self.first_name + " " + self.last_name

    def sex_long(self):
        if self.sex == 'f':
            return 'female'
        else :
            return 'male'