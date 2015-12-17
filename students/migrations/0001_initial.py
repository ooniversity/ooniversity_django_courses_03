# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ('courses', '0001_initial'),
=======
        ('courses', '0002_auto_20151128_0020'),
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
<<<<<<< HEAD
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=75)),
                ('address', models.CharField(max_length=100)),
                ('skype', models.CharField(max_length=50)),
=======
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('skype', models.CharField(max_length=255)),
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
                ('courses', models.ManyToManyField(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
