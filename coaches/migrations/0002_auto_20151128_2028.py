# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='address',
            field=models.CharField(default='dd', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coach',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2015, 11, 28)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coach',
            name='description',
            field=models.TextField(default='hhh'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coach',
            name='gender',
            field=models.CharField(default='M', max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coach',
            name='phone',
            field=models.CharField(default='222', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coach',
            name='skype',
            field=models.CharField(default='hfthf', max_length=255),
            preserve_default=False,
        ),
    ]
