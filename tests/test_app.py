from app import app


def test_get_inventory():
    client = app.test_client()

    response = client.get("/inventory")

    assert response.status_code == 200

def test_get_single_item():
    client = app.test_client()

    response = client.get("/inventory/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1

def test_create_item():
    client = app.test_client()

    new_item = {
        "name": "Chocolate Bar",
        "brand": "DairyLand",
        "price": 100,
        "stock": 25,
        "barcode": "345222333"
    }

    response = client.post("/inventory", json=new_item)

    assert response.status_code == 201

    data = response.get_json()

    assert data["name"] == "Chocolate Bar"
    assert data["price"] == 100
    assert data["stock"] == 25

def test_update_item():
    client = app.test_client()

    update_data = {
        "price": 400,
        "stock": 30
    }

    response = client.patch("/inventory/1", json=update_data)

    assert response.status_code == 200

    data = response.get_json()

    assert data["price"] == 400
    assert data["stock"] == 30

def test_delete_item():
    client = app.test_client()

    response = client.delete("/inventory/2")

    assert response.status_code == 204

def test_create_item_missing_field():
    client = app.test_client()

    invalid_item = {
        "name": "Chocolate Bar",
        "brand": "DairyLand",
        "price": 100,
        "stock": 25
    }

    response = client.post("/inventory", json=invalid_item)

    assert response.status_code == 400

    data = response.get_json()

    assert "barcode" in data["error"]

def test_create_item_invalid_price():
    client = app.test_client()

    invalid_item = {
        "name": "Chocolate Bar",
        "brand": "DailyLand",
        "price": -100,
        "stock": 25,
        "barcode": "345222333"
    }

    response = client.post("/inventory", json=invalid_item)

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Price must be greater than 0"

def test_create_item_invalid_stock():
    client = app.test_client()

    invalid_item = {
        "name": "Chocolate Bar",
        "brand": "DailyLand",
        "price": 100,
        "stock": -5,
        "barcode": "345222333"
    }

    response = client.post("/inventory", json=invalid_item)

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Stock must be 0 or greater"

def test_get_item_not_found():
    client = app.test_client()

    response = client.get("/inventory/999")

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Inventory item not found"

def test_update_item_not_found():
    client = app.test_client()

    update_data = {
        "price": 500
    }

    response = client.patch("/inventory/999", json=update_data)

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Inventory item not found"

def test_delete_item_not_found():
    client = app.test_client()

    response = client.delete("/inventory/999")

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Inventory item not found"