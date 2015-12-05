# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('courses', '0004_auto_20151124_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='subject',
        ),
    ]
