# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
