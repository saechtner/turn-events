# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0005_auto_20150315_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='club',
            field=models.ForeignKey(blank=True, null=True, to='gymnastics.Club'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='all_around_individual_counting_events',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='all_around_team_counting_events',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='discipline_finals_max_participants',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
