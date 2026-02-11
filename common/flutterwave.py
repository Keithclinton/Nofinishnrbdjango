import requests
from django.conf import settings

class FlutterwaveClient:
    def __init__(self):
        self.base_url = 'https://api.flutterwave.com/v3'
        self.secret_key = settings.FLUTTERWAVE_SECRET_KEY

    def initiate_payment(self, data):
        url = f'{self.base_url}/payments'
        headers = {
            'Authorization': f'Bearer {self.secret_key}',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def verify_payment(self, tx_ref):
        url = f'{self.base_url}/transactions/{tx_ref}/verify'
        headers = {
            'Authorization': f'Bearer {self.secret_key}'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
