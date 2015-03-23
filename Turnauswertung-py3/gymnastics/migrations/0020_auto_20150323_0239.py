# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0019_stream_discipline_finals_both_values_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='squad',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='gymnastics.Squad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='team',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='gymnastics.Team'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athletesimport',
            name='club',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='gymnastics.Club'),
            preserve_default=True,
        ),
    ]
