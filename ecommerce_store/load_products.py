import json
import requests

# Load products from the JSON file
with open('products.json', 'r') as file:
    products = json.load(file)

# URL for the POST request
url = 'http://127.0.0.1:8000/products/create/'

# Iterate over each product and send a POST request to create it
for product in products:
    print(f"Sending request data: {product}")
    response = requests.post(url, json=product)
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.text}")
    if response.status_code == 201:
        print(f"Product '{product['name']}' created successfully.")
    else:
        print(f"Failed to create product '{product['name']}'.")
