# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coach',
            old_name='desciption',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='coach',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='coach',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
