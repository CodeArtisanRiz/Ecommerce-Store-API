import json
import requests

# Load products from the JSON file
with open('orders.json', 'r') as file:
    orders = json.load(file)

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

