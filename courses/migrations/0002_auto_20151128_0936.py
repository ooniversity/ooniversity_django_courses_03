# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='Courses',
        ),
        migrations.AlterModelTable(
            name='courses',
            table='courses',
        ),
    ]
