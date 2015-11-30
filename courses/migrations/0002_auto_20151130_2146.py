# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_auto_20151130_2141'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(related_name=b'assistant_courses', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(related_name=b'coach_courses', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='subject',
            field=models.CharField(max_length=40),
        ),
    ]
