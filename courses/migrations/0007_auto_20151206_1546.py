# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20151206_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='subject',
            field=models.CharField(max_length=5000),
        ),
    ]
