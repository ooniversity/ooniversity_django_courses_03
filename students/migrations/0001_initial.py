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
                ('name', models.CharField(max_length=255, verbose_name=b'\xd0\xb8\xd0\xbc\xd1\x8f')),
                ('surname', models.CharField(max_length=255, verbose_name=b'\xd1\x84\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('date_of_birth', models.DateField(verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=255, verbose_name=b'\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd')),
                ('address', models.CharField(max_length=255, verbose_name=b'\xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81')),
                ('skype', models.CharField(max_length=255)),
                ('courses', models.ManyToManyField(to='courses.Course', verbose_name=b'\xd0\xba\xd1\x83\xd1\x80\xd1\x81\xd1\x8b, \xd0\xbd\xd0\xb0 \xd0\xba\xd0\xbe\xd1\x82\xd0\xbe\xd1\x80\xd1\x8b\xd1\x85 \xd1\x83\xd1\x87\xd0\xb8\xd1\x82\xd1\x81\xd1\x8f \xd1\x81\xd1\x82\xd1\x83\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x82')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
