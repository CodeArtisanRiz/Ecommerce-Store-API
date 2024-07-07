import json
import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load orders from a JSON file and create them via a POST request'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the JSON file containing order data')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            with open(file_path, 'r') as file:
                orders = json.load(file)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR("Error decoding JSON"))
            return

        # URL for the POST request
        url = 'http://127.0.0.1:8000/orders/create/'

        # Iterate over each product and send a POST request to create it
        for order in orders:
            print(f"Sending request data: {order}")
            response = requests.post(url, json=order)
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.text}")
            if response.status_code == 201:
                if 'customer_name' in order:
                    print(f"Order '{order['customer_name']}' created successfully.")
                else:
                    print("Order created successfully, but 'customer_name' key is missing.")
            else:
                print(f"Failed to create order.")

