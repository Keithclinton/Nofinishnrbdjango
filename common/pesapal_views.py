from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from django.conf import settings
import uuid
from common.pesapal import PesapalClient

class PesapalPaymentInitView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        pesapal = PesapalClient()
        data = request.data
        merchant_reference = str(uuid.uuid4())
        payment_data = {
            'amount': data['amount'],
            'currency': data.get('currency', 'KES'),
            'description': data.get('description', 'Payment'),
            'callback_url': settings.PESAPAL_CALLBACK_URL,
            'notification_id': merchant_reference,
            'redirect_url': settings.PESAPAL_REDIRECT_URL,
            'customer': {
                'first_name': data.get('first_name', ''),
                'last_name': data.get('last_name', ''),
                'email': data.get('email', ''),
                'phone_number': data.get('phone', ''),
            },
            'merchant_reference': merchant_reference
        }
        try:
            result = pesapal.initiate_payment(payment_data)
            return Response({'payment': result, 'merchant_reference': merchant_reference}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PesapalPaymentStatusView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, order_tracking_id):
        pesapal = PesapalClient()
        try:
            result = pesapal.query_payment_status(order_tracking_id)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PesapalCallbackView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        # Pesapal will POST payment notification here
        # You should verify and update payment/order status
        data = request.data
        # TODO: Add your order/payment update logic here
        return Response({'status': 'callback received', 'data': data}, status=status.HTTP_200_OK)
