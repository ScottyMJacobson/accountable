# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('accounts', '0003_auto_20150828_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(to='auth.Group', blank=True, verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', related_name='user_set'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', blank=True, verbose_name='user permissions', help_text='Specific permissions for this user.', related_query_name='user', related_name='user_set'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status'),
        ),
    ]
