from django.db import models

from gymnastics.models.athlete import Athlete


class Club(models.Model):
  
    name = models.CharField(max_length=50, null=False)
    

    class Meta:
        db_table = 'gymnastics_clubs'

    @property
    def athletes(self):
        return Athlete.objects.filter(club=self)
        
    def __str__(self):
        return self.name
