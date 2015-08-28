# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commitments', '0002_auto_20150828_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='commitmentstatus',
            name='comment',
            field=models.CharField(max_length=140, null=True, blank=True),
        ),
    ]
