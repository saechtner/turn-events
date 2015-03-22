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
    discipline_finals_both_values_count = models.BooleanField(blank=True, default=True)

    discipline_set = models.ManyToManyField('Discipline')



    class Meta:
        db_table = 'gymnastics_streams'
        

    def __str__(self):
        return "{0} {1}".format(self.difficulty, self.get_sex_display())


    def athletes_rank(self):
        athlete_list = sorted({athlete: athlete.performance_total() \
            for athlete in self.athlete_set.all()}.items(), key=lambda x: x[1], reverse=True)
        rank = 1
        prevTotal = athlete_list[0][1]
        ranks_dict = {}
        for athlete, total_value in athlete_list:
            if total_value < prevTotal:
                rank += 1
            ranks_dict[athlete] = rank
        return ranks_dict


    def team_rank(self):
        team_list = sorted({team: team.performance_total() \
            for team in self.team_set.all()}.items(), key=lambda x: x[1], reverse=True)
        rank = 1
        prevTotal = team_list[0][1]
        ranks_dict = {}
        for team, total_value in team_list:
            if total_value < prevTotal:
                rank += 1
            ranks_dict[team] = rank
        return ranks_dict


    def final_rank(self):
        participants = self.final_participants()
        discipline_rank_dict = {}
        for discipline in self.discipline_set.all():
            athlete_list = sorted({athlete: athlete.final_total(discipline) \
                for athlete in participants.get(discipline)}.items(), key=lambda x: x[1], reverse=True)
            rank = 1
            prevTotal = athlete_list[0][1]
            ranks_dict = {}
            for athlete, total_value in athlete_list:
                if total_value < prevTotal:
                    rank += 1
                ranks_dict[athlete] = rank
            discipline_rank_dict[discipline] = ranks_dict
        return discipline_rank_dict


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