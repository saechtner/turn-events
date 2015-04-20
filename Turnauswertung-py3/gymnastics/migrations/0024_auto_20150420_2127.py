# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0023_auto_20150418_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplineindex',
            name='position',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='minimum_year_of_birth',
            field=models.IntegerField(verbose_name='minimum Year of Birth', default=2000),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='disciplineindex',
            unique_together=set([]),
        ),
    ]
