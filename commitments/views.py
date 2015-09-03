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

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def commitments_list(request, format=None):
    """
    Get or post to the list of all commitments linked to the authenticated user
    """
    if request.method == 'GET':
        serializer = CommitmentSerializer(request.user.commitmentprofile.get_all_commitments(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommitmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user.commitmentprofile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


