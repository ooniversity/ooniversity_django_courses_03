# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0003_auto_20151213_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 13, 21, 22, 59, 555364, tzinfo=utc), auto_now_add=True),
        ),
    ]
