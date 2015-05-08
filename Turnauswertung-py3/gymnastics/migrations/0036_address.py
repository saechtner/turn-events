# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0035_auto_20150507_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('street', models.TextField(max_length=128, verbose_name='street')),
                ('city', models.TextField(max_length=128, verbose_name='city')),
                ('province', models.TextField(max_length=128, verbose_name='province')),
                ('zip_code', models.TextField(max_length=10, verbose_name='zip code')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
