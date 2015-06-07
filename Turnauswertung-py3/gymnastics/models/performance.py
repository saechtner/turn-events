from django.db import models
from django.utils.translation import ugettext_lazy

class Performance(models.Model):
  
    value = models.DecimalField(ugettext_lazy('Value'),null=False, max_digits=5, decimal_places=3, default=0.0)
    value_final = models.DecimalField(ugettext_lazy('Final Value'),null=True, blank=True, max_digits=5, decimal_places=3)
    
    athlete = models.ForeignKey('Athlete', verbose_name=ugettext_lazy('Athlete'))
    discipline = models.ForeignKey('Discipline', verbose_name=ugettext_lazy('Discipline'))



    class Meta:
        db_table = 'gymnastics_performances'
        unique_together = (("athlete", "discipline"), )

    def __str__(self):
        return "{0}, {1}".format(self.athlete, self.discipline) # old
        # return "{0}, {1}: {2}".format(self.athlete, self.discipline, self.value)
