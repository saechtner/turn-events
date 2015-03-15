from django.db import models


class Athlete(models.Model):
  
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    sex = models.CharField(max_length=1, null=False, choices=(('m', 'male'), ('f', 'female')), default='f')
    year_of_birth = models.IntegerField(default=2000)

    club = models.ForeignKey('Club', null=True, blank=True)
    squad = models.ForeignKey('Squad', null=True, blank=True)
    stream = models.ForeignKey('Stream', null=False)
    team = models.ForeignKey('Team', null=True, blank=True)


    class Meta:
        db_table = 'gymnastics_athletes'

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def sex_long(self):
        return 'female' if self.sex == 'f' else 'male'