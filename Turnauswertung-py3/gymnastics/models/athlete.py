from django.core.urlresolvers import reverse
from django.db import models
from gymnastics.models.club import Club

class Athlete(models.Model):
  
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    sex = models.CharField(max_length=1, null=False, choices=(('m', 'male'), ('f', 'female')), default='f')
    year_of_birth = models.IntegerField()
    club = models.ForeignKey(Club)

    class Meta:
        db_table = 'gymnastics_athletes'