# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0029_auto_20150504_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='contact_address',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='location',
        ),
        migrations.AddField(
            model_name='club',
            name='contact_city',
            field=models.CharField(blank=True, null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='club',
            name='contact_phone',
            field=models.CharField(blank=True, null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='club',
            name='contact_street',
            field=models.CharField(blank=True, null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='club',
            name='contact_zip_code',
            field=models.CharField(blank=True, null=True, max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tournament',
            name='city',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='street',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='zip_code',
            field=models.CharField(default='test', max_length=10),
            preserve_default=False,
        ),
    ]
