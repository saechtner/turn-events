# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0029_auto_20150504_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='date_of_birth',
            field=models.DateField(default='1900-01-01'),
            preserve_default=True,
        ),
    ]
