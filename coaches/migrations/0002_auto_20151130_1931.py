# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coach',
            old_name='descriprion',
            new_name='description',
        ),
    ]
