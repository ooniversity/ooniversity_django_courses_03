# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('courses', '0002_auto_20151126_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assistent',
            field=models.ForeignKey(related_name='assistant_courses', to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(related_name='coach_courses', to='coaches.Coach', null=True),
            preserve_default=True,
        ),
    ]
