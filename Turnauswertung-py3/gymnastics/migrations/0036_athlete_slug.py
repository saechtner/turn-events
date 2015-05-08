# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0035_auto_20150507_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='slug',
            field=models.SlugField(max_length=127, unique=True, default='<built-in function id>'),
            preserve_default=False,
        ),
    ]
