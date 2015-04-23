# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0024_auto_20150420_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamDisciplineJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('position', models.IntegerField(null=True)),
                ('discipline', models.ForeignKey(to='gymnastics.Discipline')),
                ('stream', models.ForeignKey(to='gymnastics.Stream')),
            ],
            options={
                'db_table': 'gymnastics_stream_discipline_joins',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='stream',
            name='discipline_set',
            field=models.ManyToManyField(to='gymnastics.Discipline', through='gymnastics.StreamDisciplineJoin'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='minimum_year_of_birth',
            field=models.IntegerField(default=2000),
            preserve_default=True,
        ),
    ]
