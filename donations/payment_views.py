from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from common.mpesa import MpesaClient
from django.conf import settings

class MpesaTokenView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        client = MpesaClient()
        try:
            access_token = client.get_access_token()
            return Response({"access_token": access_token})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Placeholder for C2B, B2C, STK Push, etc. endpoints
# Implement according to Safaricom API documentation as needed
