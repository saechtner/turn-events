# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0025_auto_20150423_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplineindex',
            name='discipline',
        ),
        migrations.RemoveField(
            model_name='disciplineindex',
            name='stream',
        ),
        migrations.DeleteModel(
            name='DisciplineIndex',
        ),
    ]
