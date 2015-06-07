import datetime

# from django import forms
# from django.contrib.admin.widgets import AdminDateWidget 

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy


class Tournament(models.Model):
  
    name = models.CharField(ugettext_lazy('Name'), max_length=50, default='KJSS 2015')
    name_full = models.CharField(ugettext_lazy('Full Name'), max_length=255)
    date = models.DateField(ugettext_lazy('Date'), default=datetime.date.today)
    region = models.CharField(ugettext_lazy('Region'), max_length=128, null=True, blank=True)

    management = models.CharField(ugettext_lazy('Management'), max_length=128, null=True, blank=True)
    organisation = models.CharField(ugettext_lazy('Organisation'), max_length=128, null=True, blank=True)
    calculation = models.CharField(ugettext_lazy('Calculation'), max_length=128, null=True, blank=True)
    technology = models.CharField(ugettext_lazy('Technology'), max_length=128, null=True, blank=True)
    
    address = models.ForeignKey('Address',  null=True, blank=True, verbose_name=ugettext_lazy('Address'))
    hosting_club = models.ForeignKey('Club', null=True, blank=True, verbose_name=ugettext_lazy('Hosting club'))

    slug = models.SlugField(max_length=128, blank=True)

    class Meta:
        db_table = 'gymnastics_tournaments'

    def __str__(self):
        return '{0}'.format(self.name)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = str(slugify(str(self)))
        return super(Tournament, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tournaments.detail', kwargs={ 'id': self.id, 'slug': self.slug })

    def get_edit_url(self):
        return reverse('tournaments.edit', kwargs={ 'pk': self.id, 'slug': self.slug })

    def get_delete_url(self):
        return reverse('tournaments.delete', kwargs={ 'pk': self.id, 'slug': self.slug })

    def get_evaluation_url(self):
        return reverse('tournaments.create_evaluation_pdf', kwargs={ 'id': self.id, 'slug': self.slug })

        
# TODO: add datepicker
# class MyForm(forms.Form):
#     date = forms.DateField(widget=AdminDateWidget)