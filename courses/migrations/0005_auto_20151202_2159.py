# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20151202_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='assistant',
        ),
        migrations.RemoveField(
            model_name='course',
            name='coach',
        ),
    ]
