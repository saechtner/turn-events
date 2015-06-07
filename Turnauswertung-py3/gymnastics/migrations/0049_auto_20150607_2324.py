# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0048_auto_20150606_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournament',
            old_name='organisition',
            new_name='organisation',
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
