import operator

from django.db import models
from django.utils.translation import ugettext_lazy as _

class StreamDisciplineJoin(models.Model):
    position = models.IntegerField(null=True)
    stream = models.ForeignKey('Stream')
    discipline = models.ForeignKey('Discipline')

    class Meta:
        db_table = 'gymnastics_stream_discipline_joins'


    def __str__(self):
        return "No {0}: {1} in {2}".format(self.position, self.discipline, self.stream)
