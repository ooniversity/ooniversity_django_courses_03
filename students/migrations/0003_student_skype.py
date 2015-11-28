# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20151127_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='skype',
            field=models.CharField(default=datetime.date(2015, 11, 28), max_length=200),
            preserve_default=False,
        ),
    ]
