from django.test import TestCase
from django.contrib.auth import get_user_model

from commitments.models import *

from django.utils import timezone
import datetime

class CommitmentProfileTestCase(TestCase):
    def setUp(self):
        self.username = "test_user"
        self.email = "test@email.com"
        self.password = "test_password"
        self.user =  get_user_model().objects.create_user(
                username = self.username,
                email = self.email,
                password = self.password,
            )    

    def test_user_with_profile(self):
        """make sure that the commitmentprofile gets automatically generated"""
        my_commitment_profile = self.user.commitmentprofile
        if my_commitment_profile is None:
            self.fail("Commitment profile doesn't exist")

    def test_add_commitment_to_user(self):
        dummy_commitment_name = 'brush teeth'
        dummy_commitment_description = 'brush your teeth every night'
        my_commitment_profile = self.user.commitmentprofile
        my_commitment_profile.register_commitment(dummy_commitment_name, 
            dummy_commitment_description)
        all_commitments = my_commitment_profile.get_active_commitments()
        self.assertEqual(all_commitments[0].name, dummy_commitment_name)
        self.assertEqual(all_commitments[0].description, dummy_commitment_description)


class CommitmentSnapshotTestCase(TestCase):
    def setUp(self):
        self.username = "test_user"
        self.email = "test@email.com"
        self.password = "test_password"
        self.user =  get_user_model().objects.create_user(
                username = self.username,
                email = self.email,
                password = self.password,
            )
        self.dummy_commitment_name = 'wash face'
        self.dummy_commitment_description = 'wash your face every night'
        my_commitment_profile = self.user.commitmentprofile
        my_commitment_profile.register_commitment(self.dummy_commitment_name, 
            self.dummy_commitment_description)

    def test_create_today_snapshot(self):
        snapshot = self.user.commitmentprofile.get_snapshot()
        assert snapshot
        duplicate_snapshot = self.user.commitmentprofile.get_snapshot()
        # make sure it doesn't create duplicates
        self.assertEqual(snapshot, duplicate_snapshot)
        commitment_statuses = snapshot.commitmentstatus_set.all()
        self.assertEqual(commitment_statuses[0].commitment.name,
                        self.dummy_commitment_name)

    def test_create_future_snapshot(self):
        snapshot = self.user.commitmentprofile.get_snapshot(date=datetime.date.today()+datetime.timedelta(days=1))
        assert snapshot

    def test_set_commitment_accomplished(self):
        all_commitments = self.user.commitmentprofile.get_active_commitments()
        snapshot = self.user.commitmentprofile.get_snapshot()
        commitment_to_accomplish = all_commitments[0]
        time_accomplished = timezone.now()
        snapshot.set_commitment_accomplished(commitment_to_accomplish.id, comment = "I DID IT!", time=time_accomplished)
        updated_status = snapshot.get_commitment_status_by_id(commitment_to_accomplish.id)
        self.assertEqual(updated_status.time_accomplished, time_accomplished)

    



