# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20151128_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='skype',
            field=models.CharField(max_length=255),
        ),
    ]
