# Ecommerce-Store-API
A Django Rest API project for building an ecommerce platform with a recommendation system. Features include product management, order processing, and personalized product recommendations.

## Features

- **Product Management:** Add and view products.
- **Order Processing:** Place and view orders.
- **Recommendation System:** Generate and return personalized product recommendations based on past orders and category similarities.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
    ```
    git clone https://github.com/CodeArtisanRiz/Ecommerce-Store-API.git
    cd ecommerce_store
    ```

2. **Create and activate a virtual environment:**
    ```
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```
    pip install -r requirements.txt
    ```

4. **Make migrations and migrate the database:**
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Load initial data for products and orders:**
    ```
    python manage.py load_products
    python manage.py load_orders
    ```

6. **Generate recommendations:**
    ```
    python manage.py generate_recommendations
    ```

## Running the Server

To start the development server, run:
```
python manage.py runserver
```

## End Points:
### A. Create Product:
    1. Open Postman.
    2. Set the request type to POST.
    3. Enter the endpoint URL.
```
http://127.0.0.1:8000/products/create/
```
    4. Go to the Body tab.
    5. Select raw and choose JSON from the dropdown menu.
    6. Paste the JSON request body:
```
{
      "name": "Sony Xperia",
      "status": "A",
      "category": "EL",
      "price": 19000.00,
      "description": "A high-end smartphone with amazing features.",
      "image": "path/to/image1.jpg"
}
```
    7. Click Send to create the product.
```
Response:
    {
        "message": "Product added successfully"
    }
```


### B. View a Product:

    1. Open Postman.
    2. Set the request type to GET.
    3. Enter the endpoint URL.
```
http://127.0.0.1:8000/products/{product_id}
```

    4. Click Send to view the product.
```
Example: http://127.0.0.1:8000/products/1/

Response:
    {
        "id": 1,
        "status": "NO",
        "name": "Smartphone X200",
        "category": "EL",
        "description": "A high-end smartphone with amazing features.",
        "price": 1200,
        "image": "path/to/image1.jpg",
        "created_at": "2024-07-06T18:43:51.959628Z",
        "updated_at": "2024-07-06T18:43:51.959636Z"
    }
```
### C. View all Products:

    1. Open Postman.
    2. Set the request type to GET.
    3. Enter the endpoint URL.
```
http://127.0.0.1:8000/products/view/
```

    4. Click Send to view the products.
```
Example: http://127.0.0.1:8000/products/view/

Response:
[
    {
        "id": 1,
        "status": "NO",
        "name": "Smartphone X200",
        "category": "EL",
        "description": "A high-end smartphone with amazing features.",
        "price": 1200,
        "image": "path/to/image1.jpg",
        "created_at": "2024-07-06T18:43:51.959628Z",
        "updated_at": "2024-07-06T18:43:51.959636Z"
    },
    ...
]
```

### D. Create a order:
    1. Open Postman.
    2. Set the request type to POST.
    3. Enter the endpoint URL.
```
http://127.0.0.1:8000/orders/create/
```
    4. Go to the Body tab.
    5. Select raw and choose JSON from the dropdown menu.
    6. Paste the JSON request body:
```
  {
    "customer_name": "Rajesh Kutrapalli",
    "customer_email": "raj.kp@example.com",
    "customer_phone": "987-654-3210",
    "shipping_address": "456 MG Road",
    "shipping_city": "Mumbai",
    "shipping_state": "MH",
    "shipping_zip": "400001",
    "shipping_country": "India",
    "products": [30, 15, 25],
    "total_price": 299.99,
    "payment_method": "Debit Card",
    "payment_status": "Paid",
    "status": "D"
  }
```
    7. Click Send to create the order.
```
Response:
    {
        "id": 35,
        "customer_name": "John Doe",
        "customer_email": "john.doe@example.com",
        "customer_phone": "123-456-7890",
        "shipping_address": "123 Main St",
        "shipping_city": "Springfield",
        "shipping_state": "IL",
        "shipping_zip": "62704",
        "shipping_country": "USA",
        "order_date": "2024-07-07T18:26:29.399344Z",
        "status": "P",
        "total_price": "199.99",
        "payment_method": "Credit Card",
        "payment_status": "Pending",
        "products": [
            1,
            2
        ]
    }
```

### E. View a Order:

    1. Open Postman.
    2. Set the request type to GET.
    3. Enter the endpoint URL.
```
http://127.0.0.1:8000/orders/{order_id}
```

    4. Click Send to view the order.
```
Example: http://127.0.0.1:8000/orders/1/

Response:
    {
        "id": 1,
        "customer_name": "Vikram Rathore",
        "customer_email": "vik.rathore@example.com",
        "customer_phone": "987-654-3210",
        "shipping_address": "456 MG Road",
        "shipping_city": "Mumbai",
        "shipping_state": "MH",
        "shipping_zip": "400001",
        "shipping_country": "India",
        "order_date": "2024-07-06T18:52:44.776157Z",
        "status": "D",
        "total_price": "299.99",
        "payment_method": "Debit Card",
        "payment_status": "Paid",
        "products": [
            15,
            25,
            30
        ]
    }
```
### F. View all Orders:

    1. Open Postman.
    2. Set the request type to GET.
    3. Enter the endpoint URL.
```
http://127.0.0.1:8000/orders/all/
```

    4. Click Send to view the orders.
```
Example: http://127.0.0.1:8000/orders/all/

Response:
[
    {
        "id": 1,
        "customer_name": "Vikram Rathore",
        "customer_email": "vik.rathore@example.com",
        "customer_phone": "987-654-3210",
        "shipping_address": "456 MG Road",
        "shipping_city": "Mumbai",
        "shipping_state": "MH",
        "shipping_zip": "400001",
        "shipping_country": "India",
        "order_date": "2024-07-06T18:52:44.776157Z",
        "status": "D",
        "total_price": "299.99",
        "payment_method": "Debit Card",
        "payment_status": "Paid",
        "products": [
            15,
            25,
            30
        ]
    },
    ...
]
```
### G. Create Bulk Products from JSON:

```
python manage.py load_products link.json
```
    Example:
    python manage.py load_products single_pro.json

### H. Create Bulk Orders from JSON:

```
python manage.py load_orders link.json
```
    Example:
    python manage.py load_orders single_order.json

### I. Create Recommendations:

```
python manage.py generate_recommendations
```
    Example:
    python manage.py load_orders single_order.json

### J. View recommendations

    1. Open Postman.
    2. Set the request type to GET.
    3. Enter the endpoint URL:
    http://127.0.0.1:8000/recommendations/{product_id}/
    4. Click Send to view the orders.
```
Example: http://127.0.0.1:8000/recommendations/35/
Response:
{
    "product": {
        "id": 35,
        "name": "Wireless Printer",
        "category": "OF",
        "price": 1300,
        "image": "path/to/image15.jpg"
    },
    "recommended_products": [
        {
            "id": 7,
            "name": "Latest Bestseller Novel",
            "category": "BK",
            "price": 1100,
            "image": "path/to/image7.jpg"
        },
        {
            "id": 16,
            "name": "Fitness Tracker",
            "category": "HG",
            "price": 1400,
            "image": "path/to/image16.jpg"
        },
        {
            "id": 21,
            "name": "Smartphone X200",
            "category": "EL",
            "price": 1200,
            "image": "path/to/image1.jpg"
        },
        {
            "id": 25,
            "name": "Ergonomic Office Chair",
            "category": "OF",
            "price": 1250,
            "image": "path/to/image5.jpg"
        },
        {
            "id": 15,
            "name": "Wireless Printer",
            "category": "OF",
            "price": 1300,
            "image": "path/to/image15.jpg"
        }
    ]
}
```