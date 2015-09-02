from django.test import TestCase
from django.contrib.auth import get_user_model

from commitments.serializers import CommitmentDailySnapshotSerializer,\
                                        CommitmentProfileSerializer, \
                                        CommitmentSerializer, \
                                        CommitmentStatusSerializer

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
        self.dummy_commitment_name = 'wash face'
        self.dummy_commitment_description = 'wash your face every night'
        self.dummy_commitment_name2 = 'wash face2'
        self.dummy_commitment_description2 = 'wash your face every night2'

        my_commitment_profile = self.user.commitmentprofile
        my_commitment_profile.register_commitment(self.dummy_commitment_name, 
            self.dummy_commitment_description)
        my_commitment_profile.register_commitment(self.dummy_commitment_name2, 
            self.dummy_commitment_description2)

    def test_commitment_profile_serializer(self):
        self.serializer = CommitmentProfileSerializer(self.user.commitmentprofile)
        self.assertEqual(self.serializer.data['user'], self.user.commitmentprofile.id)

    def test_commitment_profile_serializer_with_snapshot(self):
        snapshot = self.user.commitmentprofile.get_snapshot()
        assert snapshot
        self.serializer = CommitmentProfileSerializer(self.user.commitmentprofile)
        self.assertEqual(self.serializer.data['commitmentdailysnapshot_set'][0], snapshot.id)


class CommitmentSerializerTestCase(TestCase):
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
        self.dummy_commitment = self.user.commitmentprofile.get_active_commitments()[0]

    def test_commitment_serializer(self):
        self.serializer = CommitmentSerializer(self.dummy_commitment)
        self.assertEqual(self.serializer.data['name'], self.dummy_commitment_name)
        self.assertEqual(self.serializer.data['owner'], self.user.id)


class CommitmentDailySnapshotSerializerTestCase(TestCase):
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
        self.dummy_commitment = self.user.commitmentprofile.get_active_commitments()[0]

    def test_commitment_daily_snapshot_serializer(self):
        snapshot = self.user.commitmentprofile.get_snapshot()
        assert snapshot
        self.serializer = CommitmentDailySnapshotSerializer(snapshot)
        self.assertEqual(self.serializer.data['owner'], self.user.commitmentprofile.id)

class CommitmentStatusSerializerTestCase(TestCase):
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
        self.dummy_commitment = self.user.commitmentprofile.get_active_commitments()[0]
        self.snapshot = self.user.commitmentprofile.get_snapshot()

    def test_commitment_status_serializer(self):
        self.serializer = CommitmentStatusSerializer(self.snapshot.get_commitment_status_by_id(self.dummy_commitment.id))
        print(self.serializer.data)



