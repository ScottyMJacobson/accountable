from rest_framework import serializers

from commitments.models import CommitmentProfile, Commitment, CommitmentDailySnapshot, CommitmentStatus

class CommitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commitment
        fields = ('name', 'owner', 'created', 'modified', 'name', 'description', 'due_time')


class CommitmentProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = CommitmentProfile
        fields = ('user', 'commitment_set', 'commitmentdailysnapshot_set')


class CommitmentDailySnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitmentDailySnapshot
        fields = ('date', 'commitmentstatus_set', 'owner')
        