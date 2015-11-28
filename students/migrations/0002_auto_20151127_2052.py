# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=datetime.date(2015, 11, 27), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
