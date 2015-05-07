# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0033_auto_20150505_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='name_full',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
