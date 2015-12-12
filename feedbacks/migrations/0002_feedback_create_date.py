# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='create_date',
            field=models.DateTimeField(default=datetime.date(2015, 12, 12), auto_now_add=True),
            preserve_default=False,
        ),
    ]
