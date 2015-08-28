from django.db import models
from django.conf import settings
import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

class CommitmentProfile(models.Model):
    """The profile of a user, which contains the commitments they have created as well as their progress on each"""
    # Optional because there are users who will be observers who don't have a commitment profile...
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True)

class Commitment(models.Model):
    """A single commitment, with a name and description (and eventually, frequency, alert settings, etc)"""
    owner = models.ForeignKey(CommitmentProfile)
    created = models.DateTimeField(default=datetime.datetime.now, blank=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    due_time = models.TimeField(default=datetime.time(hour=23, minute=59))


class CommitmentDailySnapshot(models.Model):
    """A representation of one day's worth of commitments and how each has done""" 
    date = models.DateField()
    owner = models.ForeignKey(CommitmentProfile)


class CommitmentStatus(models.Model):
    """The progress of one specific commitment on one specific day"""
    commitment = models.ForeignKey(Commitment)
    parent_snapshot = models.ForeignKey(CommitmentDailySnapshot)
    #NULL IF NOT YET ACCOMPLISHED
    time_accomplished = models.DateTimeField(blank=True, null=True)




