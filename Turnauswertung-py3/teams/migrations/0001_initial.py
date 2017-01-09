# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-09 06:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubs', '0001_initial'),
        ('streams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.Club', verbose_name='Club')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streams.Stream', verbose_name='Stream')),
            ],
        ),
    ]
