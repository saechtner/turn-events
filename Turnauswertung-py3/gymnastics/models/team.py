from django.core.urlresolvers import reverse
from django.db import models

from gymnastics.models.stream import Stream

class Team(models.Model):
  
    name = models.CharField(max_length=50, null=False)

    stream = models.ForeignKey('Stream', null=False)


    class Meta:
        db_table = 'gymnastics_teams'    

    def __str__(self):
        return "{0} ({1})".format(self.name, self.stream)