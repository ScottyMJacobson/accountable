from django.db import models
from django.conf import settings
import datetime

# The profile of a user, which contains the commitments they have created as well as their progress on each
class CommitmentProfile(models.Model):
    # Optional because there are users who will be observers who don't have a commitment profile...
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True)


# A single commitment, with a name and description (and eventually, frequency, alert settings, etc)
class Commitment(models.Model):
    owner = models.ForeignKey(CommitmentProfile)
    created = models.DateTimeField(default=datetime.datetime.now, blank=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    due_time = models.TimeField(default=datetime.time(hour=23, minute=59))


# A representation of one day's worth of commitments and how each has done
class CommitmentDailySnapshot(models.Model):
    date = models.DateField()
    owner = models.ForeignKey(CommitmentProfile)


# The progress of one specific commitment on one specific day
class CommitmentStatus(models.Model):
    commitment = models.ForeignKey(Commitment)
    parent_snapshot = models.ForeignKey(CommitmentDailySnapshot)
    #time accomplished - NULL IF NOT YET ACCOMPLISHED
    time_accomplished = models.DateTimeField(blank=True, null=True)




