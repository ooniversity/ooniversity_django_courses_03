# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20151126_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='skype',
            field=models.CharField(max_length=50),
        ),
    ]
