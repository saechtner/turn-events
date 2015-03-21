# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0015_auto_20150318_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='value_final',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=4),
            preserve_default=True,
        ),
    ]
