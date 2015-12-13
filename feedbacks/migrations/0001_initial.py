# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('from_email', models.EmailField(max_length=75)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2015, 12, 13, 12, 51, 53, 784496, tzinfo=utc), auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
