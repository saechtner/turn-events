# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0036_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='contact_name',
            field=models.CharField(verbose_name='Contact name', max_length=64, default='none'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(verbose_name='City', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='province',
            field=models.CharField(verbose_name='Province', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(verbose_name='Street', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(verbose_name='Zip code', max_length=10),
            preserve_default=True,
        ),
    ]
