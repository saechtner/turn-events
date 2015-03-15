# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0011_auto_20150315_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='club',
            field=models.ForeignKey(to='gymnastics.Club', null=True, blank=True),
            preserve_default=True,
        ),
    ]
