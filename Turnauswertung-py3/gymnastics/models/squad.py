import itertools

from django.db import models


class Squad(models.Model):
  
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'gymnastics_squads'

    def __str__(self):
        return self.name

    def get_disciplines(self, athletes=None):
        if not athletes:
            athletes = self.athlete_set.all() \
                .select_related('stream') \
                .prefetch_related('stream__discipline_set')

        streams_distinct = athletes.get_distinct_stream_set()
        streams_disciplines = itertools.chain.from_iterable((stream.discipline_set.all() for stream in streams_distinct))
        return list(set(streams_disciplines))

    def get_stream_disciplines_dict(self, athletes=None):
        if not athletes:
            athletes = self.athlete_set.all() \
                .select_related('stream') \
                .prefetch_related('stream__discipline_set')

        streams_distinct = athletes.get_distinct_stream_set()
        return { stream.id: stream.get_ordered_disciplines() for stream in streams_distinct }

    def get_stream_athletes_dict(self, athletes=None):
        if not athletes:
            athletes = self.athlete_set.all() \
                .select_related('club').select_related('stream').select_related('team__stream').select_related('squad') \
                .prefetch_related('performance_set')

        streams_distinct = athletes.get_distinct_stream_set()
        stream_athletes_dict = { stream.id: [] for stream in streams_distinct }
        for athlete in athletes:
            stream_athletes_dict[athlete.stream.id].append(athlete)

        return stream_athletes_dict
