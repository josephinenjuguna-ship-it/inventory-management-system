from flask import Flask, jsonify, request
from inventory import inventory
from validation import validate_inventory_item, validate_inventory_update

app = Flask(__name__)


@app.get("/inventory")
def get_inventory():
    return jsonify(inventory)

@app.get("/inventory/<int:item_id>")
def get_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item)

    return jsonify({"error": "Inventory item not found"}), 404

@app.post("/inventory")
def create_item():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    error = validate_inventory_item(data)

    if error:
        return jsonify({"error": error}), 400

    new_item = {
       "id": max(item["id"] for item in inventory) + 1 if inventory else 1,
        "name": data["name"],
        "brand": data["brand"],
        "price": data["price"],
        "stock": data["stock"],
        "barcode": data["barcode"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

@app.patch("/inventory/<int:item_id>")
def update_item(item_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    for item in inventory:
        if item["id"] == item_id:

            error = validate_inventory_update(data)

            if error:
                return jsonify({"error": error}), 400

            if "name" in data:
                item["name"] = data["name"]

            if "brand" in data:
                item["brand"] = data["brand"]

            if "price" in data:
                item["price"] = data["price"]

            if "stock" in data:
                item["stock"] = data["stock"]

            if "barcode" in data:
                item["barcode"] = data["barcode"]

            return jsonify(item), 200

    return jsonify({"error": "Inventory item not found"}), 404

@app.delete("/inventory/<int:item_id>")
def delete_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return "", 204

    return jsonify({"error": "Inventory item not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)