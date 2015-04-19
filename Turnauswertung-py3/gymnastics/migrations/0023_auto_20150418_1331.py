# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0022_auto_20150418_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplineIndex',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('discipline', models.ForeignKey(to='gymnastics.Discipline')),
                ('stream', models.ForeignKey(to='gymnastics.Stream')),
            ],
            options={
                'db_table': 'gymnastics_discipline_indices',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='disciplineindex',
            unique_together=set([('stream', 'discipline', 'position')]),
        ),
        migrations.AddField(
            model_name='stream',
            name='discipline_set',
            field=models.ManyToManyField(through='gymnastics.DisciplineIndex', to='gymnastics.Discipline'),
            preserve_default=True,
        ),
    ]
