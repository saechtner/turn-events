# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymnastics', '0037_auto_20150508_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='slug',
            field=models.SlugField(blank=True, max_length=127),
            preserve_default=True,
        ),
    ]
