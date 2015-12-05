# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('courses', '0003_auto_20151124_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
