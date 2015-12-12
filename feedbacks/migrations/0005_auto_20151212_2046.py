# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0004_auto_20151212_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='surname',
            new_name='subject',
        ),
    ]
