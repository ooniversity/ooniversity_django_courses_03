# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20151127_1753'),
        ('students', '0002_auto_20151127_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('package', models.CharField(max_length=50)),
                ('subscribe', models.BooleanField()),
                ('comment', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('courses', models.ForeignKey(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
