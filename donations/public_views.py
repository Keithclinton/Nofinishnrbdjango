from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Donation
from .serializers import DonationSerializer

class PublicDonationCreateView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        donation_data = {
            'amount': data.get('amount'),
            'payment_method': data.get('paymentMethod', ''),
            'first_name': data.get('firstName', ''),
            'last_name': data.get('lastName', ''),
            'email': data.get('email', ''),
            'phone': data.get('phone', ''),
            'is_recurring': data.get('isRecurring', False),
        }
        serializer = DonationSerializer(data=donation_data)
        if serializer.is_valid():
            donation = serializer.save()
            return Response({'success': True, 'donation_id': donation.id}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
