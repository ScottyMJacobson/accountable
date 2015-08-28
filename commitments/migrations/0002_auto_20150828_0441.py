# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commitments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommitmentDailySnapshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommitmentProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user', models.OneToOneField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommitmentStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time_accomplished', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='commitment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AddField(
            model_name='commitment',
            name='due_time',
            field=models.TimeField(default=datetime.time(23, 59)),
        ),
        migrations.AddField(
            model_name='commitmentstatus',
            name='commitment',
            field=models.ForeignKey(to='commitments.Commitment'),
        ),
        migrations.AddField(
            model_name='commitmentstatus',
            name='parent_snapshot',
            field=models.ForeignKey(to='commitments.CommitmentDailySnapshot'),
        ),
        migrations.AddField(
            model_name='commitment',
            name='owner',
            field=models.ForeignKey(default=None, to='commitments.CommitmentProfile'),
            preserve_default=False,
        ),
    ]
