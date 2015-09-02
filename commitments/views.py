from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from commitments.models import CommitmentProfile, \
                                        Commitment, \
                                        CommitmentDailySnapshot, \
                                        CommitmentStatus

from commitments.serializers import CommitmentDailySnapshotSerializer,\
                                        CommitmentProfileSerializer, \
                                        CommitmentSerializer, \
                                        CommitmentStatusSerializer



@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def commitment_profile(request, format=None):
    """
    Get the commitment profile for the currently authenticated
    user
    """
    if request.method == 'GET':
        current_profile = request.user.commitmentprofile
        serializer = CommitmentProfileSerializer(current_profile)
        return Response(serializer.data)

