# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0046_remove_athlete_year_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='region',
            field=models.CharField(null=True, blank=True, max_length=128),
            preserve_default=True,
        ),
    ]
