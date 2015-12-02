# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_courseapplication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseapplication',
            old_name='courses',
            new_name='course',
        ),
    ]
