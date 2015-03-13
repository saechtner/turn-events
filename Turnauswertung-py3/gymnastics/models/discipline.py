from django.db import models

class Discipline(models.Model):

  class Meta:
    db_table = 'gymnastics_disciplines'
  
  name = models.CharField(max_length=50, null=False)