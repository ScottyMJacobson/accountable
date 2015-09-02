from rest_framework import serializers

from commitments.models import CommitmentProfile, Commitment, CommitmentDailySnapshot, CommitmentStatus

class CommitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commitment
        fields = ('name', 'owner', 'created', 'modified', 'name', 'description', 'due_time')


