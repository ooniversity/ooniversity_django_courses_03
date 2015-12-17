# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20151202_2159'),
        ('coaches', '0004_remove_coach_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coach',
        ),
    ]
