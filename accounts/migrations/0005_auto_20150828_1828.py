# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150828_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='joined',
            new_name='date_joined',
        ),
    ]
