# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0044_auto_20150510_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='slug',
            field=models.SlugField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discipline',
            name='slug',
            field=models.SlugField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tournament',
            name='slug',
            field=models.SlugField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
