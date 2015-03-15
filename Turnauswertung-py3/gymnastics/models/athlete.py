from django.core.urlresolvers import reverse
from django.db import models
from gymnastics.models.club import Club

class Athlete(models.Model):
  
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    sex = models.CharField(max_length=1, null=False, choices=(('m', 'male'), ('f', 'female')), default='f')
    year_of_birth = models.IntegerField(default=2000)

    club = models.ForeignKey(Club, null=True, blank=True)


    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = 'gymnastics_athletes'