# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0018_athletesimport_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='discipline_finals_both_values_count',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
