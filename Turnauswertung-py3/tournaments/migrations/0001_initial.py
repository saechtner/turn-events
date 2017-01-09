# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-09 06:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='KJSS 2015', max_length=50, verbose_name='Name')),
                ('name_full', models.CharField(max_length=255, verbose_name='Full Name')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('region', models.CharField(blank=True, max_length=128, null=True, verbose_name='Region')),
                ('management', models.CharField(blank=True, max_length=128, null=True, verbose_name='Management')),
                ('organisation', models.CharField(blank=True, max_length=128, null=True, verbose_name='Organisation')),
                ('calculation', models.CharField(blank=True, max_length=128, null=True, verbose_name='Calculation')),
                ('technology', models.CharField(blank=True, max_length=128, null=True, verbose_name='Technology')),
                ('slug', models.SlugField(blank=True, max_length=128)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Address', verbose_name='Address')),
                ('hosting_club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.Club', verbose_name='Hosting club')),
            ],
        ),
    ]
