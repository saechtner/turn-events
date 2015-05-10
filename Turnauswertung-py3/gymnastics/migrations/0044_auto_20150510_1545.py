# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0043_auto_20150510_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='contact_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='contact_phone',
            new_name='phone',
        ),
    ]
