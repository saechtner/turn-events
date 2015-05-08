# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0036_athlete_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='slug',
            field=models.SlugField(max_length=127),
            preserve_default=True,
        ),
    ]
