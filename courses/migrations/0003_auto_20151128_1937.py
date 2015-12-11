# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0002_remove_coach_is_staff'),
        ('courses', '0002_auto_20151124_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(related_name='assistant_courses', blank=True, to='coaches.Coach', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(related_name='coach_courses', blank=True, to='coaches.Coach', null=True),
        ),
    ]
