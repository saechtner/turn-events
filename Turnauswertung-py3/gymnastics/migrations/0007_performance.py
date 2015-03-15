# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0006_auto_20150315_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('performance', models.DecimalField(max_digits=4, decimal_places=2)),
                ('athlete', models.ForeignKey(to='gymnastics.Athlete')),
                ('discipline', models.ForeignKey(to='gymnastics.Discipline')),
            ],
            options={
                'db_table': 'gymnastics_performances',
            },
            bases=(models.Model,),
        ),
    ]
