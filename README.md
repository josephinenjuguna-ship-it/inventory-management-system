# inventory-management-system
Flask inventory management system with OpenFoodFacts API integration
# Inventory Management System

A beginner-friendly retail inventory management system built with Python and Flask.

The system provides a REST API for managing inventory, integrates with the OpenFoodFacts API for product lookup, and includes a command-line interface (CLI) for interacting with the inventory.

## Features

1. View all inventory items
2. View a single inventory item
3. Add a new inventory item
4. Update an inventory item's price and stock
5. Delete an inventory item
6. Validate inventory data
7. Search OpenFoodFacts by barcode
8. Search OpenFoodFacts by product name
9. Handle missing products and API failures
10. Command-line interface for inventory management
11. Automated tests using pytest
12. Simulated inventory storage using a Python list

## Technologies Used

* Python
* Flask
* Requests
* Pytest
* OpenFoodFacts API

## Project Structure

```text
inventory-management-system/
│
├── app.py
├── inventory.py
├── validation.py
├── external_api.py
├── cli.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── tests/
    ├── __init__.py
    ├── test_app.py
    └── test_external_api.py
```

### File Descriptions

 File                    Purpose                                          

 `app.py`                Contains the Flask REST API and CRUD routes      
 `inventory.py`          Stores the simulated inventory data              
 `validation.py`         Contains validation rules for inventory data     
 `external_api.py`       Handles OpenFoodFacts API requests               
 `cli.py`                Provides the command-line interface              
 `test_app.py`           Tests the Flask inventory API                    
 `test_external_api.py`  Tests OpenFoodFacts integration and API failures 
 `requirements.txt`      Lists project dependencies                       

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/josephinenjuguna-ship-it/inventory-management-system.git
```

Move into the project directory:

```bash
cd inventory-management-system
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

On Linux/macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Flask API

Start the Flask application with:

```bash
python app.py
```

The API will run locally, usually at:

```text
http://127.0.0.1:5000
```

You can test the API using tools such as Thunder Client, Postman, or curl.

## API Endpoints

### Get all inventory

**GET**

```text
/inventory
```

Example:

```bash
curl http://127.0.0.1:5000/inventory
```

Returns all inventory items.

### Get one inventory item

**GET**

```text
/inventory/<id>
```

Example:

```bash
curl http://127.0.0.1:5000/inventory/1
```

Returns the inventory item with the specified ID.

If the item does not exist, the API returns:

```text
404 Not Found
```

### Add an inventory item

**POST**

```text
/inventory
```

Example JSON body:

```json
{
    "name": "Chocolate Bar",
    "brand": "DairyLand",
    "price": 100,
    "stock": 25,
    "barcode": "345222333"
}
```

Example using curl:

```bash
curl -X POST http://127.0.0.1:5000/inventory \
-H "Content-Type: application/json" \
-d '{"name":"Chocolate Bar","brand":"DailyLand","price":100,"stock":25,"barcode":"345222333"}'
```

A successful request returns:

```text
201 Created
```

### Update an inventory item

**PATCH**

```text
/inventory/<id>
```

Example:

```json
{
    "price": 120,
    "stock": 30
}
```

Example using curl:

```bash
curl -X PATCH http://127.0.0.1:5000/inventory/1 \
-H "Content-Type: application/json" \
-d '{"price":120,"stock":30}'
```

A successful request returns:

```text
200 OK
```

### Delete an inventory item

**DELETE**

```text
/inventory/<id>
```

Example:

```bash
curl -X DELETE http://127.0.0.1:5000/inventory/1
```

A successful deletion returns:

```text
204 No Content
```

### Error Responses

The API handles common errors such as:

| Status Code | Meaning                                         |
| ----------- | ----------------------------------------------- |
| `200`       | Request successful                              |
| `201`       | Inventory item created                          |
| `204`       | Item deleted successfully with no response body |
| `400`       | Invalid or missing input                        |
| `404`       | Inventory item not found                        |

## Command-Line Interface

The project also provides an interactive CLI.

Start it with:

```bash
python cli.py
```

The menu provides:

```text
===== INVENTORY MANAGEMENT SYSTEM =====
1. View all inventory
2. View one item
3. Add item
4. Update item
5. Delete item
6. Find product on Open Food Facts
7. Exit
```

### View all inventory

Choose:

```text
1
```

The CLI displays the available inventory items, including their IDs, prices, and stock levels.

### View one item

Choose:

```text
2
```

Enter the item ID when prompted.

Example:

```text
Enter item ID: 1
```

### Add an item

Choose:

```text
3
```

The CLI asks for:

* Product name
* Brand
* Price
* Stock
* Barcode

The input is validated before the item is added.

### Update an item

Choose:

```text
4
```

Enter the item ID and provide a new price or stock value.

Pressing Enter without entering a new value keeps the current value.

### Delete an item

Choose:

```text
5
```

Enter the ID of the item you want to delete.

### Find a product on OpenFoodFacts

Choose:

```text
6
```

The CLI provides two search methods:

```text
===== FIND PRODUCT =====
1. Search by barcode
2. Search by name
```

For example, a barcode search can use:

```text
3017624010701
```

The system displays the product name, brand, and barcode when a product is found.

The CLI also handles products that cannot be found and temporary API failures without crashing.

## OpenFoodFacts Integration

The application uses OpenFoodFacts to retrieve product information.

The integration supports:

* Barcode searches
* Product name searches
* Handling products that are not found
* Handling temporary API failures

The external API functionality is contained in:

```text
external_api.py
```

## Running Tests

The project uses pytest for automated testing.

Run all tests with:

```bash
pytest
```

The test suite covers:

* Inventory CRUD operations
* Input validation
* Missing inventory items
* Invalid prices
* Invalid stock values
* OpenFoodFacts barcode lookup
* OpenFoodFacts name lookup
* Product-not-found responses
* API failure responses

## Maintainability

The project separates responsibilities across different files:

* Flask routes are kept in `app.py`
* Inventory data is kept in `inventory.py`
* Validation logic is kept in `validation.py`
* External API logic is kept in `external_api.py`
* CLI functionality is kept in `cli.py`
* Tests are kept in the `tests/` directory

This separation makes the code easier to understand, test, maintain, and extend.

The application also uses clear function names, descriptive error messages, input validation, and comments where they help explain the purpose of the code.

## Future Improvements

Possible future improvements include:

* Replace the simulated Python list with a real database
* Add user authentication and authorization
* Add  inventory search
* Add more detailed product information from OpenFoodFacts
* Add a web-based administrator dashboard
* Add more automated CLI tests
* Add logging for API errors and inventory operations

## Author

Josephine Njuguna
