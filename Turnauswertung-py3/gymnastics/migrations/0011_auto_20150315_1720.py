# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0010_team_stream'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stream',
            name='all_around_team_counting_events',
        ),
        migrations.AddField(
            model_name='stream',
            name='all_around_team_counting_athletes',
            field=models.IntegerField(null=True, blank=True, default=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='performance',
            name='performance',
            field=models.DecimalField(max_digits=4, decimal_places=2, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='all_around_individual_counting_events',
            field=models.IntegerField(null=True, blank=True, default=4),
            preserve_default=True,
        ),
    ]
