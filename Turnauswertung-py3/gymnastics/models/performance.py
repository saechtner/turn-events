from django.db import models

class Performance(models.Model):
  
    value = models.DecimalField(null=False, max_digits=5, decimal_places=3, default=0.0)
    value_final = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=3)
    
    athlete = models.ForeignKey('Athlete')
    discipline = models.ForeignKey('Discipline')



    class Meta:
        db_table = 'gymnastics_performances'
        unique_together = (("athlete", "discipline"), )

    def __str__(self):
        return "{0}, {1}".format(self.athlete, self.discipline) # old
        # return "{0}, {1}: {2}".format(self.athlete, self.discipline, self.value)
