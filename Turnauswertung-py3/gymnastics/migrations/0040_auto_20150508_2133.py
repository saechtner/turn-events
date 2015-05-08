# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0039_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='contact_name',
            field=models.CharField(max_length=64, verbose_name='Contact name', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squad',
            name='slug',
            field=models.SlugField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=128, verbose_name='City'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='province',
            field=models.CharField(max_length=128, verbose_name='Province'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=128, verbose_name='Street'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=10, verbose_name='Zip code'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='slug',
            field=models.SlugField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
