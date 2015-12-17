# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField()),
<<<<<<< HEAD
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('skype', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
=======
                ('gender', models.CharField(max_length=6, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('skype', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
