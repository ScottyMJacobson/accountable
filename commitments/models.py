from django.db import models
from django.conf import settings
import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

DEFAULT_DUE_TIME = datetime.time(hour=23, minute=59)

class CommitmentProfile(models.Model):
    """The profile of a user, which contains the commitments they have created as well as their progress on each"""
    # Optional because there are users who will be observers who don't have a commitment profile...
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True)

    def register_commitment(self, name, description, due_time=DEFAULT_DUE_TIME):
        """Add a commitment to this profile"""
        new_commitment = Commitment.objects.create(
                                    owner_id = self.id, 
                                    name = name,
                                    description = description,
                                    due_time = due_time
                                )
        new_commitment.save()

    def get_active_commitments(self):
        return self.commitment_set.all()

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return "Commitment Profile for {0}".format(user.username)


# make sure that with every new user, a commitmentprofile gets made
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_commitmentprofile(sender, instance, created, **kwargs):
    if created:
        CommitmentProfile.objects.create(user=instance)


class Commitment(models.Model):
    """A single commitment, with a name and description (and eventually, frequency, alert settings, etc)"""
    owner = models.ForeignKey(CommitmentProfile)
    created = models.DateTimeField(default=datetime.datetime.now, blank=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    due_time = models.TimeField(default=DEFAULT_DUE_TIME)
    
    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return "{0}: due {1} at {2}".format(self.name, "daily", self.due_time)


class CommitmentDailySnapshot(models.Model):
    """A representation of one day's worth of commitments and how each has done""" 
    date = models.DateField(default = datetime.date.today)
    owner = models.ForeignKey(CommitmentProfile)


class CommitmentStatus(models.Model):
    """The progress of one specific commitment on one specific day"""
    commitment = models.ForeignKey(Commitment)
    parent_snapshot = models.ForeignKey(CommitmentDailySnapshot)
    #NULL IF NOT YET ACCOMPLISHED
    time_accomplished = models.DateTimeField(blank=True, null=True)




