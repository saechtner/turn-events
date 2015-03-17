# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0013_performance_performance_final'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stream',
            old_name='disciplines',
            new_name='discipline_set',
        ),
    ]
