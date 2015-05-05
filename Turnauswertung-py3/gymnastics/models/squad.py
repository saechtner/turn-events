from django.db import models

class Squad(models.Model):
  
    name = models.CharField(max_length=50, null=False)


    class Meta:
        db_table = 'gymnastics_squads'
    
    def __str__(self):
        return self.name

    def get_stream_athletes_and_disciplines_dict(self, athletes=None):
        if not athletes:
            athletes = self.athlete_set.all() \
                .select_related('club').select_related('stream').select_related('team__stream').select_related('squad') \
                .prefetch_related('performance_set')

        streams_distinct = set([athlete.stream for athlete in athletes])
        stream_athletes_and_disciplines_dict = { 
            stream.id: {
                'athletes': [], 
                'disciplines': stream.ordered_disciplines.all()
            } for stream in streams_distinct 
        }
        for athlete in athletes:
            stream_athletes_and_disciplines_dict[athlete.stream.id]['athletes'].append(athlete)

        return stream_athletes_and_disciplines_dict