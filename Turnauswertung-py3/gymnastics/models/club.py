from django.db import models

# from gymnastics.models.athlete import Athlete
# from gymnastics.models.club import Club
# from gymnastics.models.squad import Squad
# from gymnastics.models.stream import Stream
# from gymnastics.models.team import Team


class Club(models.Model):
  
    name = models.CharField(max_length=50, null=False)
    

    class Meta:
        db_table = 'gymnastics_clubs'

    def __str__(self):
        return self.name

    def authors(self):
        return Athlete.objects.filter(club = self)