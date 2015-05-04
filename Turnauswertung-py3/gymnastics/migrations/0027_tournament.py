# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0026_auto_20150423_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('location', models.TextField()),
                ('club', models.ForeignKey(verbose_name='Host', null=True, to='gymnastics.Club')),
            ],
            options={
                'db_table': 'gymnastics_tournaments',
            },
            bases=(models.Model,),
        ),
    ]
