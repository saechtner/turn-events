# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0040_auto_20150508_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squad',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Squad'),
            preserve_default=True,
        ),
    ]
