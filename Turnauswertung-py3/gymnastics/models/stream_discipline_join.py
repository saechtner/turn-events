from django.db import models


class StreamDisciplineJoin(models.Model):
    position = models.IntegerField(null=True)
    
    stream = models.ForeignKey('streams.Stream')
    discipline = models.ForeignKey('Discipline')

    class Meta:
        db_table = 'gymnastics_stream_discipline_joins'
        ordering = ['position']

    def __str__(self):
        return "No {0}: {1} in {2}".format(self.position, self.discipline, self.stream)
