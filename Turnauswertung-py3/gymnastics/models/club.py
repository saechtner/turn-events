from django.db import models


class Club(models.Model):
  
    name = models.CharField(max_length=50)

    address = models.ForeignKey('Address', null=True, blank=True)


    class Meta:
        db_table = 'gymnastics_clubs'

    def __str__(self):
        return self.name