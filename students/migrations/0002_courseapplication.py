# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('package', models.CharField(max_length=50, choices=[(b'standart', b'Standart'), (b'gold', b'Gold'), (b'vip', b'VIP')])),
                ('subscribe', models.BooleanField()),
                ('comment', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
