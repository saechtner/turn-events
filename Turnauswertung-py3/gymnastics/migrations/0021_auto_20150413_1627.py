# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0020_auto_20150323_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='value_final',
            field=models.DecimalField(decimal_places=2, blank=True, max_digits=4, null=True),
            preserve_default=True,
        ),
    ]
