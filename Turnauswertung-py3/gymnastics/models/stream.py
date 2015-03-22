from django.db import models

from gymnastics.models.discipline import Discipline

class Stream(models.Model):
  
    difficulty = models.CharField(max_length=10, null=False)
    sex = models.CharField(max_length=1, null=False, choices=(('m', 'male'), ('f', 'female')), default='f')
    minimum_year_of_birth = models.IntegerField(default=2000, null=False)
    
    all_around_individual = models.BooleanField(default=True)
    all_around_individual_counting_events = models.IntegerField(null=True, blank=True, default=4)
    all_around_team = models.BooleanField(default=True)
    all_around_team_counting_athletes = models.IntegerField(null=True, blank=True, default=4)
    discipline_finals = models.BooleanField(default=False)
    discipline_finals_max_participants = models.IntegerField(null=True, blank=True)

    discipline_set = models.ManyToManyField('Discipline')



    class Meta:
        db_table = 'gymnastics_streams'
        

    def __str__(self):
        return "{0} {1}".format(self.difficulty, self.get_sex_display())


    def athletes_rank(self):
        athlete_dict = {}
        for athlete in self.athlete_set.all():
            performance_total = athlete.performance_total()
            if performance_total == None:
                performance_total = -1
            if not athlete_dict.get(performance_total):
                athlete_dict[performance_total] = []

            athlete_dict[performance_total].append(athlete)

        rank = 0
        ranks_dict = {}  
        for total_value, athlete_list in sorted(athlete_dict.items(), reverse=True):
            rank += 1
            if total_value < 0:
                rank = None
            for athlete_object in athlete_list:
                ranks_dict[athlete_object] = rank

        return ranks_dict


    def team_rank(self):
        team_dict = {}
        for team in self.team_set.all():
            performance_total = team.performance_total()
            if performance_total == None:
                performance_total = -1
            if not team_dict.get(performance_total):
                team_dict[performance_total] = []
            team_dict[performance_total].append(team)

        rank = 0
        ranks_dict = {}  
        for total_value, team_list in sorted(team_dict.items(), reverse=True):
            rank += 1
            if total_value < 0:
                rank = None
            for team_object in team_list:
                ranks_dict[team_object] = rank

        return ranks_dict


    def finals_rank(self):
        return {}


    def final_participants(self):
        participants_dict = {}
        for discipline in self.discipline_set.all():
            discipline_performances = {}
            for athlete in self.athlete_set.all():
                athlete_performance = athlete.performances()[discipline]
                if not discipline_performances.get(athlete_performance):
                    discipline_performances[athlete_performance] = []
                discipline_performances[athlete_performance].append(athlete)

            participants_dict[discipline] = []
            for value, athlete_list in sorted(discipline_performances.items(), reverse=True):
                participants_dict[discipline].extend(athlete_list)
                if len(participants_dict[discipline]) >= self.discipline_finals_max_participants:
                    break

        return participants_dict