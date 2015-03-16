# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0012_team_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='performance_final',
            field=models.DecimalField(decimal_places=2, max_digits=4, default=0.0),
            preserve_default=True,
        ),
    ]
