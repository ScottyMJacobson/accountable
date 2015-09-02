# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('commitments', '0004_auto_20150830_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commitmentprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
