from django.db import models

class Sportart(models.Model):
  
  name = models.CharField(max_length=50, null=False)