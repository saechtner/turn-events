# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0041_auto_20150508_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='contact_city',
        ),
        migrations.RemoveField(
            model_name='club',
            name='contact_mail',
        ),
        migrations.RemoveField(
            model_name='club',
            name='contact_name',
        ),
        migrations.RemoveField(
            model_name='club',
            name='contact_phone',
        ),
        migrations.RemoveField(
            model_name='club',
            name='contact_street',
        ),
        migrations.RemoveField(
            model_name='club',
            name='contact_zip_code',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='city',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='street',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='address',
            name='contact_email',
            field=models.EmailField(blank=True, null=True, verbose_name='Contact email', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='contact_phone',
            field=models.CharField(blank=True, null=True, verbose_name='Contact phone', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='club',
            name='address',
            field=models.ForeignKey(blank=True, null=True, to='gymnastics.Address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tournament',
            name='address',
            field=models.ForeignKey(blank=True, null=True, to='gymnastics.Address'),
            preserve_default=True,
        ),
    ]
