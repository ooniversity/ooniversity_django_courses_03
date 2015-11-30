# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0002_auto_20151129_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='address',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='coach',
            name='skype',
            field=models.CharField(max_length=40),
        ),
    ]
