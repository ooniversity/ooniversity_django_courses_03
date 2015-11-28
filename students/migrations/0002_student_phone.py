# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(default=b'12-34-56', max_length=20),
            preserve_default=True,
        ),
    ]
