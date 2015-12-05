# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20151128_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.CharField(max_length=50),
        ),
    ]
