# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0002_club'),
    ]

    operations = [
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'gymnastics_squads',
            },
            bases=(models.Model,),
        ),
    ]
