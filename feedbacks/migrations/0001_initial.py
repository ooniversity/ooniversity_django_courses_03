# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=120)),
                ('from_email', models.CharField(max_length=80)),
                ('message', models.TextField()),
                ('create_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
