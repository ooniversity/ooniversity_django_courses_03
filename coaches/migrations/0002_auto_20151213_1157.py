# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='coach',
            name='gender',
            field=models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='coach',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='coach',
            name='skype',
            field=models.CharField(max_length=50),
        ),
    ]
