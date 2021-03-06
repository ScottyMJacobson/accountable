from rest_framework import serializers

from commitments.models import CommitmentProfile, Commitment, CommitmentDailySnapshot, CommitmentStatus

class CommitmentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField()
    class Meta:
        model = Commitment
        fields = ('id', 'name', 'owner', 'created', 'modified', 'name', 'description', 'due_time')


class CommitmentProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = CommitmentProfile
        fields = ('user', 'commitment_set', 'commitmentdailysnapshot_set')


class CommitmentStatusSerializer(serializers.ModelSerializer):
    commitment = CommitmentSerializer(read_only=True)

    class Meta:
        model = CommitmentStatus
        fields = ('id','commitment', 'parent_snapshot', 'time_accomplished', 'comment')


class CommitmentDailySnapshotSerializer(serializers.ModelSerializer):
    commitmentstatus_set = CommitmentStatusSerializer(many=True)
    class Meta:
        model = CommitmentDailySnapshot
        fields = ('id', 'date', 'commitmentstatus_set', 'owner')


