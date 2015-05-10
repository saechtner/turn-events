# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0042_auto_20150510_0207'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='address',
            table='gymnastics_addresses',
        ),
    ]
