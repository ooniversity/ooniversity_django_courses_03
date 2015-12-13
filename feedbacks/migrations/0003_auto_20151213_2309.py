# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0002_auto_20151213_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 13, 21, 9, 7, 950115, tzinfo=utc), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='from_email',
            field=models.EmailField(max_length=75, verbose_name=b'Your e-mail'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Your name'),
        ),
    ]
