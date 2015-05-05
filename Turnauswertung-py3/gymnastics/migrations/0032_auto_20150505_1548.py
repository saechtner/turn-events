# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0031_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='contact_street',
            field=models.CharField(blank=True, null=True, max_length=100),
            preserve_default=True,
        ),
    ]
