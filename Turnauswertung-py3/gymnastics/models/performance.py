from django.db import models

class Performance(models.Model):
  
    performance = models.DecimalField(null=False, max_digits=4, decimal_places=2, default=0.0)
    
    athlete = models.ForeignKey('Athlete')
    discipline = models.ForeignKey('Discipline')


    class Meta:
        db_table = 'gymnastics_performances'

    def __str__(self):
        return self.athlete + ", " + self.discipline + ": " + self.performance