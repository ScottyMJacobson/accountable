# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import annoying.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commitment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('due_time', models.TimeField(default=datetime.time(23, 59))),
            ],
        ),
        migrations.CreateModel(
            name='CommitmentDailySnapshot',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='CommitmentProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('user', annoying.fields.AutoOneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommitmentStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('time_accomplished', models.DateTimeField(null=True, blank=True)),
                ('comment', models.CharField(null=True, max_length=140, blank=True)),
                ('commitment', models.ForeignKey(to='commitments.Commitment')),
                ('parent_snapshot', models.ForeignKey(to='commitments.CommitmentDailySnapshot')),
            ],
        ),
        migrations.AddField(
            model_name='commitmentdailysnapshot',
            name='owner',
            field=models.ForeignKey(to='commitments.CommitmentProfile'),
        ),
        migrations.AddField(
            model_name='commitment',
            name='owner',
            field=models.ForeignKey(to='commitments.CommitmentProfile'),
        ),
    ]
