# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20151129_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='assistent',
            new_name='assistant',
        ),
    ]
