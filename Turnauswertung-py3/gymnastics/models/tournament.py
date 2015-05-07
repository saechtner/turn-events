import datetime

# from django import forms
# from django.contrib.admin.widgets import AdminDateWidget 

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy


class Tournament(models.Model):
  
    name = models.CharField(max_length=50, default='KJSS 2015')
    name_full = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)

    street = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)

    hosting_club = models.ForeignKey('Club', null=True, blank=True)

    class Meta:
        db_table = 'gymnastics_tournaments'

    def __str__(self):
        return '{0}'.format(self.name)

    def get_absolute_url(self):
        return reverse('tournaments.detail', kwargs={ 'id': self.id })

        
# TODO: add datepicker
# class MyForm(forms.Form):
#     date = forms.DateField(widget=AdminDateWidget)