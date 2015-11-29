# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='coach',
            name='gender',
            field=models.CharField(default=b'M', max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
