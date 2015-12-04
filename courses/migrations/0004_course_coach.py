# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0002_auto_20151203_2332'),
        ('courses', '0003_auto_20151127_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(to='coaches.Coach', null=True),
            preserve_default=True,
        ),
    ]
