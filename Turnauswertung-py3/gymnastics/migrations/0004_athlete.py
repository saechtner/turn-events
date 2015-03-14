# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0003_squad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=1, choices=[('m', 'male'), ('f', 'female')])),
                ('year_of_birth', models.IntegerField()),
                ('club', models.ForeignKey(to='gymnastics.Club')),
            ],
            options={
                'db_table': 'gymnastics_athletes',
            },
            bases=(models.Model,),
        ),
    ]
