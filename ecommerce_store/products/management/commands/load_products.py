import json
import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load products from a JSON file and create them via a POST request'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the JSON file containing product data')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            with open(file_path, 'r') as file:
                products = json.load(file)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR("Error decoding JSON"))
            return

        # URL for the POST request
        url = 'http://127.0.0.1:8000/products/create/'

        # Iterate over each product and send a POST request to create it
        for product in products:
            self.stdout.write(f"Sending request data: {product}")
            response = requests.post(url, json=product)
            self.stdout.write(f"Response status code: {response.status_code}")
            self.stdout.write(f"Response content: {response.text}")
            if response.status_code == 201:
                self.stdout.write(self.style.SUCCESS(f"Product '{product['name']}' created successfully."))
            else:
                self.stdout.write(self.style.ERROR(f"Failed to create product '{product['name']}'."))

