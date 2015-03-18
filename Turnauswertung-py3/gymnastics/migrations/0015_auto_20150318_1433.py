# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0014_auto_20150317_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performance',
            old_name='performance',
            new_name='value',
        ),
        migrations.RenameField(
            model_name='performance',
            old_name='performance_final',
            new_name='value_final',
        ),
    ]
