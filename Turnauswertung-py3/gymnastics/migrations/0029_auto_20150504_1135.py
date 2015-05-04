# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0028_auto_20150504_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='contact_adress',
        ),
        migrations.AddField(
            model_name='club',
            name='contact_address',
            field=models.TextField(blank=True, max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stream',
            name='all_around_team_size',
            field=models.IntegerField(blank=True, default=4, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='club',
            name='contact_mail',
            field=models.EmailField(blank=True, max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='club',
            name='contact_name',
            field=models.CharField(blank=True, max_length=50, null=True),
            preserve_default=True,
        ),
    ]
