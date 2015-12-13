# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0005_auto_20151212_2046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='massage',
            new_name='message',
        ),
    ]
