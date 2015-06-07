# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0047_tournament_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='calculation',
            field=models.CharField(max_length=128, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tournament',
            name='management',
            field=models.CharField(max_length=128, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tournament',
            name='organisition',
            field=models.CharField(max_length=128, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tournament',
            name='technology',
            field=models.CharField(max_length=128, blank=True, null=True),
            preserve_default=True,
        ),
    ]
