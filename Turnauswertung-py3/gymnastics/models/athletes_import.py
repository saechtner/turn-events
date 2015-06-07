from django.db import models
from django.utils.translation import ugettext_lazy


class AthletesImport(models.Model):
  
    # TODO:: add field created_at(datetime) as attribute to describe an import

    # name = models.CharField(max_length=50, null=False)

    club = models.OneToOneField('Club', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=ugettext_lazy('Club'))    

    class Meta:
        db_table = 'gymnastics_athletes_imports'

    def __str__(self):
        return '{0} #{1}'.format(ugettext_lazy('Athletes Import'),self.id)
