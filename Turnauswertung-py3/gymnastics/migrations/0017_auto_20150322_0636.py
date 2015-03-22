# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0016_auto_20150321_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='AthletesImport',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
            options={
                'db_table': 'gymnastics_athletes_imports',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='athlete',
            name='athletes_import',
            field=models.ForeignKey(to='gymnastics.AthletesImport', blank=True, null=True),
            preserve_default=True,
        ),
    ]
