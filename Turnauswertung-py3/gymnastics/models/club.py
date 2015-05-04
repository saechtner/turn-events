from django.db import models

from gymnastics.models.athlete import Athlete


class Club(models.Model):
  
    name = models.CharField(max_length=50, null=False)
    contact_name = models.CharField(max_length=50, null=True, blank=True)
    contact_mail = models.EmailField(null=True, blank=True)
    contact_address = models.TextField(max_length=50, null=True, blank=True)


    class Meta:
        db_table = 'gymnastics_clubs'

    def __str__(self):
        return self.name
