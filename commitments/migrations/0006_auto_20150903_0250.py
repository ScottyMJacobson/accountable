# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('commitments', '0005_auto_20150901_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commitmentprofile',
            name='user',
            field=annoying.fields.AutoOneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
