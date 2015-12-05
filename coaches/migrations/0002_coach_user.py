# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='user',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
