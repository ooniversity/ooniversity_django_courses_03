# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0002_auto_20151128_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='email',
            field=models.EmailField(default='eugene.n@namecheap.com', max_length=75),
            preserve_default=False,
        ),
    ]
