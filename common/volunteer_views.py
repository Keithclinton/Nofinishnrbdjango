from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .volunteer_serializers import VolunteerApplicationSerializer

class VolunteerApplicationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = VolunteerApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'Application submitted!'}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
