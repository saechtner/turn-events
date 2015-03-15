# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0008_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='squad',
            field=models.ForeignKey(blank=True, to='gymnastics.Squad', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='athlete',
            name='stream',
            field=models.ForeignKey(default=1, to='gymnastics.Stream'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='athlete',
            name='team',
            field=models.ForeignKey(blank=True, to='gymnastics.Team', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stream',
            name='minimum_year_of_birth',
            field=models.IntegerField(default=2000),
            preserve_default=True,
        ),
    ]
