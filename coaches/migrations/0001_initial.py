# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=255, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('phone', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('skype', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
