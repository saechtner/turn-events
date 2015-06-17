# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0049_auto_20150607_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='squad_position',
            field=models.IntegerField(blank=True, default=0, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='club',
            field=models.ForeignKey(verbose_name='Club', to='gymnastics.Club', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='date_of_birth',
            field=models.DateField(verbose_name='Date of birth', default='1900-01-01'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='first_name',
            field=models.CharField(verbose_name='First name', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='last_name',
            field=models.CharField(verbose_name='Last name', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='sex',
            field=models.CharField(verbose_name='Sex', max_length=1, default='f', choices=[('m', 'male'), ('f', 'female')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='squad',
            field=models.ForeignKey(verbose_name='Squad', to='gymnastics.Squad', blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='stream',
            field=models.ForeignKey(verbose_name='Stream', to='gymnastics.Stream'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='team',
            field=models.ForeignKey(verbose_name='Team', to='gymnastics.Team', blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='athletesimport',
            name='club',
            field=models.OneToOneField(verbose_name='Club', to='gymnastics.Club', blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='club',
            name='address',
            field=models.ForeignKey(verbose_name='Address', to='gymnastics.Address', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='discipline',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='performance',
            name='athlete',
            field=models.ForeignKey(verbose_name='Athlete', to='gymnastics.Athlete'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='performance',
            name='discipline',
            field=models.ForeignKey(verbose_name='Discipline', to='gymnastics.Discipline'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='performance',
            name='value',
            field=models.DecimalField(verbose_name='Value', max_digits=5, default=0.0, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='performance',
            name='value_final',
            field=models.DecimalField(verbose_name='Final Value', decimal_places=3, max_digits=5, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='all_around_individual',
            field=models.BooleanField(verbose_name='All around individual', default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='all_around_team',
            field=models.BooleanField(verbose_name='All around team', default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='difficulty',
            field=models.CharField(verbose_name='Difficulty', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='discipline_finals',
            field=models.BooleanField(verbose_name='Discipline finals', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='minimum_year_of_birth',
            field=models.IntegerField(verbose_name='Minimum Year of Birth', default=2000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='sex',
            field=models.CharField(verbose_name='Sex', max_length=1, default='f', choices=[('m', 'male'), ('f', 'female')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='club',
            field=models.ForeignKey(verbose_name='Club', to='gymnastics.Club', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='stream',
            field=models.ForeignKey(verbose_name='Stream', to='gymnastics.Stream'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='address',
            field=models.ForeignKey(verbose_name='Address', to='gymnastics.Address', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='calculation',
            field=models.CharField(verbose_name='Calculation', blank=True, max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='date',
            field=models.DateField(verbose_name='Date', default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='hosting_club',
            field=models.ForeignKey(verbose_name='Hosting club', to='gymnastics.Club', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='management',
            field=models.CharField(verbose_name='Management', blank=True, max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=50, default='KJSS 2015'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name_full',
            field=models.CharField(verbose_name='Full Name', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='organisation',
            field=models.CharField(verbose_name='Organisation', blank=True, max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='region',
            field=models.CharField(verbose_name='Region', blank=True, max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='technology',
            field=models.CharField(verbose_name='Technology', blank=True, max_length=128, null=True),
            preserve_default=True,
        ),
    ]
