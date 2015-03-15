# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0009_auto_20150315_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='stream',
            field=models.ForeignKey(to='gymnastics.Stream', default=1),
            preserve_default=False,
        ),
    ]
