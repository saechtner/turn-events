# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0017_auto_20150322_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='athletesimport',
            name='club',
            field=models.OneToOneField(blank=True, null=True, to='gymnastics.Club'),
            preserve_default=True,
        ),
    ]
