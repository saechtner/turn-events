from django.core.urlresolvers import reverse
from django.db import models

class Club(models.Model):
  
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'gymnastics_clubs'