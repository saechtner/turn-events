from django.core.urlresolvers import reverse
from django.db import models
from gymnastics.models.stream import Stream

class Team(models.Model):
  
    name = models.CharField(max_length=50, null=False)

    stream = models.ForeignKey(Stream, null=False)
    
    def __str__(self):
        return self.name #+ "(" + self.stream + ")"

    class Meta:
        db_table = 'gymnastics_teams'