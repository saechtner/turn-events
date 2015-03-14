from django.core.urlresolvers import reverse
from django.db import models

class Discipline(models.Model):
  
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'gymnastics_disciplines'

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})