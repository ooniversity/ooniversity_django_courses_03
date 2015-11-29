# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=90)),
                ('phone', models.CharField(default=b'80-80-80', max_length=30)),
                ('short_description', models.CharField(max_length=100)),
                ('skype', models.CharField(max_length=30)),
                ('courses', models.ManyToManyField(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
