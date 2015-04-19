# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0021_auto_20150413_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stream',
            name='discipline_set',
        ),
        migrations.AlterUniqueTogether(
            name='performance',
            unique_together=set([('athlete', 'discipline')]),
        ),
    ]
