from django.db import models


class AthletesImport(models.Model):
  
    # TODO:: add field created_at(datetime) as attribute to describe an import

    # name = models.CharField(max_length=50, null=False)

    club = models.OneToOneField('Club', null=True, blank=True, on_delete=models.SET_NULL)    

    class Meta:
        db_table = 'gymnastics_athletes_imports'

    def __str__(self):
        return 'Import #{}'.format(self.id)
