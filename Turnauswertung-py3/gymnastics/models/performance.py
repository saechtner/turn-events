from django.db import models

class Performance(models.Model):
  
    value = models.DecimalField(null=False, max_digits=4, decimal_places=2, default=0.0)
    value_final = models.DecimalField(null=False, max_digits=4, decimal_places=2, default=0.0)
    
    athlete = models.ForeignKey('Athlete')
    discipline = models.ForeignKey('Discipline')


    class Meta:
        db_table = 'gymnastics_performances'

    def __str__(self):
        return "{0}, {1}: {2}".format(self.athlete, self.discipline, self.performance)