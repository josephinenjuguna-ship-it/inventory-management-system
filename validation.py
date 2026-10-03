def validate_inventory_item(data):
    required_fields = ["name", "brand", "price", "stock", "barcode"]

    for field in required_fields:
        if field not in data:
            return f"{field} is required"

    if not isinstance(data["name"], str) or not data["name"].strip():
        return "Name cannot be empty"

    if not isinstance(data["brand"], str) or not data["brand"].strip():
        return "Brand cannot be empty"

    if not isinstance(data["barcode"], str) or not data["barcode"].strip():
        return "Barcode cannot be empty"

    if not isinstance(data["price"], (int, float)) or data["price"] <= 0:
        return "Price must be greater than 0"

    if not isinstance(data["stock"], int) or data["stock"] < 0:
        return "Stock must be 0 or greater"

    return None

def validate_inventory_update(data):
    allowed_fields = ["name", "brand", "price", "stock", "barcode"]

    for field in data:
        if field not in allowed_fields:
            return f"{field} cannot be updated"

    if "name" in data:
        if not isinstance(data["name"], str) or not data["name"].strip():
            return "Name cannot be empty"

    if "brand" in data:
        if not isinstance(data["brand"], str) or not data["brand"].strip():
            return "Brand cannot be empty"

    if "barcode" in data:
        if not isinstance(data["barcode"], str) or not data["barcode"].strip():
            return "Barcode cannot be empty"

    if "price" in data:
        if not isinstance(data["price"], (int, float)) or data["price"] <= 0:
            return "Price must be greater than 0"

    if "stock" in data:
        if not isinstance(data["stock"], int) or data["stock"] < 0:
            return "Stock must be 0 or greater"

    return None