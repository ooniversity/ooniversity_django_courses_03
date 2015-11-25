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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=50)),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('surname', models.CharField(verbose_name='Фамилия', max_length=50)),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('email', models.EmailField(verbose_name='email', max_length=75)),
                ('phone', models.CharField(verbose_name='Телефон', max_length=30)),
                ('address', models.CharField(verbose_name='Адрес', max_length=100)),
                ('skype', models.CharField(verbose_name='skype', max_length=30)),
                ('courses', models.ManyToManyField(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
