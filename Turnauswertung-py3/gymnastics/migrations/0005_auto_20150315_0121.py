# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0004_athlete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('difficulty', models.CharField(max_length=10)),
                ('sex', models.CharField(default='f', max_length=1, choices=[('m', 'male'), ('f', 'female')])),
                ('all_around_individual', models.BooleanField(default=True)),
                ('all_around_individual_counting_events', models.IntegerField(null=True)),
                ('all_around_team', models.BooleanField(default=True)),
                ('all_around_team_counting_events', models.IntegerField(null=True)),
                ('discipline_finals', models.BooleanField(default=False)),
                ('discipline_finals_max_participants', models.IntegerField(null=True)),
                ('disciplines', models.ManyToManyField(to='gymnastics.Discipline')),
            ],
            options={
                'db_table': 'gymnastics_streams',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='sex',
            field=models.CharField(default='f', max_length=1, choices=[('m', 'male'), ('f', 'female')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='year_of_birth',
            field=models.IntegerField(default=2000),
            preserve_default=True,
        ),
    ]
