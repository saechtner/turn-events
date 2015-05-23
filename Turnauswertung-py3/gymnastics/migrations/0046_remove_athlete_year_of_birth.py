# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0045_auto_20150510_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='year_of_birth',
        ),
    ]
