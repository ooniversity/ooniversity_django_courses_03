# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20151129_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseapplication',
            name='course',
        ),
        migrations.DeleteModel(
            name='CourseApplication',
        ),
    ]
