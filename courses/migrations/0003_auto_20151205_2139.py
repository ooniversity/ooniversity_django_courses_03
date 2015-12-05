# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20151130_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
