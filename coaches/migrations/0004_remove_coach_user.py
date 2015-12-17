# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_auto_20151202_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='user',
        ),
    ]
