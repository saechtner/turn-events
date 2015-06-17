# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0050_auto_20150617_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='squad_position',
            field=models.IntegerField(default=-1, blank=True, null=True),
            preserve_default=True,
        ),
    ]
