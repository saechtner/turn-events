import datetime

from django import forms
from django.contrib.admin.widgets import AdminDateWidget 
from django.db import models
from django.utils.translation import ugettext_lazy


class Tournament(models.Model):
  
    name = models.CharField(max_length=50, null=False)
    date = models.DateField(null=False, default=datetime.date.today)

    street = models.CharField(max_length=50, null=False)
    zip_code = models.CharField(max_length=10, null=False)
    city = models.CharField(max_length=50, null=False)

    club = models.ForeignKey('Club', verbose_name=ugettext_lazy('Host'), null=True, blank=True)

    class Meta:
        db_table = 'gymnastics_tournaments'

    def __str__(self):
        return '{0}'.format(self.name)

        
# TODO: add datepicker
# class MyForm(forms.Form):
#     date = forms.DateField(widget=AdminDateWidget)