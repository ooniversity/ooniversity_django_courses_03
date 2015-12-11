# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20151129_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseapplication',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='courseapplication',
            name='package',
            field=models.CharField(max_length=50, choices=[(b'standart', b'Standart'), (b'gold', b'Gold'), (b'vip', b'VIP')]),
        ),
    ]
