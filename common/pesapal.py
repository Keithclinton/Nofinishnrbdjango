import requests
from django.conf import settings

class PesapalClient:
    def __init__(self):
        self.base_url = 'https://pay.pesapal.com/v3/api'
        self.consumer_key = settings.PESAPAL_CONSUMER_KEY
        self.consumer_secret = settings.PESAPAL_CONSUMER_SECRET
        self.token = self.get_access_token()

    def get_access_token(self):
        url = f'{self.base_url}/Auth/RequestToken'
        data = {
            'consumer_key': self.consumer_key,
            'consumer_secret': self.consumer_secret
        }
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json().get('token')

    def initiate_payment(self, data):
        url = f'{self.base_url}/Transactions/SubmitOrderRequest'
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def query_payment_status(self, order_tracking_id):
        url = f'{self.base_url}/Transactions/GetTransactionStatus?orderTrackingId={order_tracking_id}'
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
