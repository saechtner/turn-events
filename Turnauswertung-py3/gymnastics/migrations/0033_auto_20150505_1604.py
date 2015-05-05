# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0032_auto_20150505_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='club',
        ),
        migrations.AddField(
            model_name='tournament',
            name='hosting_club',
            field=models.ForeignKey(blank=True, to='gymnastics.Club', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='street',
            field=models.CharField(blank=True, max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10, null=True),
            preserve_default=True,
        ),
    ]
