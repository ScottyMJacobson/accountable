# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commitments', '0005_auto_20150901_2138'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommitmentProfile',
            new_name='AccountableUser',
        ),
    ]
