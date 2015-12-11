# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0003_auto_20151210_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.CharField(max_length=255),
        ),
    ]
