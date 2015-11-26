# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('short_description', models.CharField(max_length=255, verbose_name=b'\xd0\xba\xd1\x80\xd0\xb0\xd1\x82\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('description', models.TextField(verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=255, verbose_name=b'\xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0')),
                ('description', models.TextField(verbose_name=b'\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('order', models.PositiveIntegerField(verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xbf\xd0\xbe \xd0\xbf\xd0\xbe\xd1\x80\xd1\x8f\xd0\xb4\xd0\xba\xd1\x83')),
                ('course', models.ForeignKey(verbose_name=b'\xd0\xba\xd1\x83\xd1\x80\xd1\x81', to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
