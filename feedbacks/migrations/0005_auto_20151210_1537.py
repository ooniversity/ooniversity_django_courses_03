# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0004_auto_20151210_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(),
        ),
    ]
