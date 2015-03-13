from django.db import models

class Sportart(models.Model):

  class Meta:
    app_label = 'turnapp'
  
  name = models.CharField(max_length=50, null=False)