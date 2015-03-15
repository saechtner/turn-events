from django.db import models

class Discipline(models.Model):
  
    name = models.CharField(max_length=50, null=False)


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'gymnastics_disciplines'