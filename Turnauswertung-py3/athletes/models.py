from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy


class AthleteQuerySet(models.QuerySet):

    def get_distinct_stream_set(self):
        return set((athlete.stream for athlete in self))

    def get_athletes_disciplines_result_dict(self):
        athletes_disciplines_result_dict = { athlete.id: athlete.get_disciplines_result_dict() for athlete in self }

        for athlete in self:
            athletes_disciplines_result_dict[athlete.id]['total'] = athlete.get_all_around_result()

        return athletes_disciplines_result_dict


class AthleteManager(models.Manager):

    def get_queryset(self):
        return AthleteQuerySet(self.model, using=self._db)


class Athlete(models.Model):

    first_name = models.CharField(ugettext_lazy('First name'), max_length=50)
    last_name = models.CharField(ugettext_lazy('Last name'), max_length=50)
    sex = models.CharField(ugettext_lazy('Sex'), max_length=1, choices=(('m', 'male'), ('f', 'female')), default='f')
    date_of_birth = models.DateField(ugettext_lazy('Date of birth'), default='1900-01-01')

    club = models.ForeignKey('gymnastics.Club', null=True, blank=True, verbose_name=ugettext_lazy('Club'))
    stream = models.ForeignKey('gymnastics.Stream', verbose_name=ugettext_lazy('Stream'))
    team = models.ForeignKey('gymnastics.Team', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=ugettext_lazy('Team'))
    squad = models.ForeignKey('gymnastics.Squad', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=ugettext_lazy('Squad'))
    squad_position = models.IntegerField(default=-1, null=True, blank=True)

    athletes_import = models.ForeignKey('AthletesImport', null=True, blank=True)

    slug = models.SlugField(max_length=128, blank=True)

    objects = AthleteManager()

    class Meta:
        db_table = 'gymnastics_athletes'

    def __str__(self):
        # Dev Output
        # return 'Athlete: [name: {0} {1}, sex: {2}, date_of_birth: {3}, club; {4}, stream: {5}]'.format( \
        #     self.first_name, self.last_name, self.sex, self.date_of_birth, self.club, self.stream)
        return '{0} {1}'.format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = str(slugify(str(self)))
        return super(Athlete, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('athletes.detail', kwargs={ 'id': self.id, 'slug': self.slug })

    def get_edit_url(self):
        return reverse('athletes.edit', kwargs={ 'pk': self.id, 'slug': self.slug })

    def get_delete_url(self):
        return reverse('athletes.delete', kwargs={ 'pk': self.id, 'slug': self.slug })

    def get_disciplines_result_dict(self):
        return { perf.discipline_id: perf.value for perf in self.performance_set.all() }

    def get_all_around_result(self):
        results_sorted = sorted((perf.value for perf in self.performance_set.all()), reverse=True)
        return sum(results_sorted[:self.stream.all_around_individual_counting_events])


    # TODO:: rework!
    def final_total(self, discipline):
        total = 0
        if self.stream.discipline_finals_both_values_count:
            total += self.performances().get(discipline)
        x = self.performances_final().get(discipline)
        if x != None:
            total += x
        return total


class AthletesImport(models.Model):

    # TODO:: add field created_at(datetime) as attribute to describe an import

    # name = models.CharField(max_length=50, null=False)

    club = models.OneToOneField('gymnastics.Club', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=ugettext_lazy('Club'))

    class Meta:
        db_table = 'gymnastics_athletes_imports'

    def __str__(self):
        return '{0} #{1}'.format(ugettext_lazy('Athletes Import'), self.id)
