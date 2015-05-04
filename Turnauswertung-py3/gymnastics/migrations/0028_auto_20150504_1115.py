# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0027_tournament'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='contact_adress',
            field=models.TextField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='club',
            name='contact_mail',
            field=models.EmailField(max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='club',
            name='contact_name',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='performance',
            name='value',
            field=models.DecimalField(default=0.0, decimal_places=3, max_digits=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='performance',
            name='value_final',
            field=models.DecimalField(max_digits=5, blank=True, null=True, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='club',
            field=models.ForeignKey(verbose_name='Host', to='gymnastics.Club', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
    ]
