# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0002_auto_20151130_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='description',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='coach',
            name='gender',
            field=models.CharField(max_length=255, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='coach',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]
