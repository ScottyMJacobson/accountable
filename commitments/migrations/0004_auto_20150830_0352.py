# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('commitments', '0003_commitmentstatus_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='commitment',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 30, 3, 52, 9, 460680, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commitment',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
