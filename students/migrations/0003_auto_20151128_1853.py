# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_courses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='adress',
            new_name='address',
        ),
    ]
