from inventory import inventory
from external_api import find_product_by_barcode, find_product_by_name

def show_menu():
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. View all inventory")
    print("2. View one item")
    print("3. Add item")
    print("4. Update item")
    print("5. Delete item")
    print("6. Find product on Open Food Facts")
    print("7. Exit")


def view_inventory():
    print("\n===== INVENTORY =====")

    for item in inventory:
        print(
            f"{item['id']}. {item['name']} - "
            f"Ksh {item['price']} - "
            f"Stock: {item['stock']}"
        )


def view_one_item():
    print("\n===== VIEW ITEM =====")

    try:
        item_id = int(input("Enter item ID: "))
    except ValueError:
        print("Invalid item ID. Please enter a number.")
        return

    for item in inventory:
        if item["id"] == item_id:
            print("\n===== ITEM =====")
            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Brand: {item['brand']}")
            print(f"Price: Ksh {item['price']}")
            print(f"Stock: {item['stock']}")
            print(f"Barcode: {item['barcode']}")
            return

    print("Inventory item not found.")

def add_item():
    print("\n===== ADD ITEM =====")

    name = input("Enter product name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return

    brand = input("Enter brand: ").strip()
    if not brand:
        print("Brand cannot be empty.")
        return

    try:
        price = float(input("Enter price: "))

        if price <= 0:
            print("Price must be greater than 0.")
            return

    except ValueError:
        print("Invalid price. Please enter a number.")
        return

    try:
        stock = int(input("Enter stock: "))

        if stock < 0:
            print("Stock cannot be negative.")
            return

    except ValueError:
        print("Invalid stock. Please enter a whole number.")
        return

    barcode = input("Enter barcode: ").strip()
    if not barcode:
        print("Barcode cannot be empty.")
        return

    new_item = {
        "id": max(item["id"] for item in inventory) + 1 if inventory else 1,
        "name": name,
        "brand": brand,
        "price": price,
        "stock": stock,
        "barcode": barcode
    }

    inventory.append(new_item)

    print("\nItem added successfully!")
    print(new_item)

def update_item():
    print("\n===== UPDATE ITEM =====")

    try:
        item_id = int(input("Enter item ID: "))
    except ValueError:
        print("Invalid item ID. Please enter a number.")
        return

    for item in inventory:
        if item["id"] == item_id:

            new_price = input(
                f"Enter new price (current: {item['price']}): "
            ).strip()

            if new_price:
                try:
                    new_price = float(new_price)

                    if new_price <= 0:
                        print("Price must be greater than 0.")
                        return

                except ValueError:
                    print("Invalid price. Please enter a number.")
                    return

            new_stock = input(
                f"Enter new stock (current: {item['stock']}): "
            ).strip()

            if new_stock:
                try:
                    new_stock = int(new_stock)

                    if new_stock < 0:
                        print("Stock cannot be negative.")
                        return

                except ValueError:
                    print("Invalid stock. Please enter a whole number.")
                    return

            if new_price:
                item["price"] = new_price

            if new_stock:
                item["stock"] = new_stock

            print("\nItem updated successfully!")
            print(item)
            return

    print("Inventory item not found.")


def delete_item():
    print("\n===== DELETE ITEM =====")

    try:
        item_id = int(input("Enter item ID: "))
    except ValueError:
        print("Invalid item ID. Please enter a number.")
        return

    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)

            print("\nItem deleted successfully!")
            return

    print("Inventory item not found.")

def find_product():
    print("\n===== FIND PRODUCT =====")
    print("1. Search by barcode")
    print("2. Search by name")

    choice = input("Choose search method: ").strip()

    if choice == "1":
        barcode = input("Enter product barcode: ").strip()

        if not barcode:
            print("Barcode cannot be empty.")
            return

        product = find_product_by_barcode(barcode)

    elif choice == "2":
        name = input("Enter product name: ").strip()

        if not name:
            print("Product name cannot be empty.")
            return

        product = find_product_by_name(name)

    else:
        print("Invalid search option.")
        return

    if product is None:
        print("Product not found or API is currently unavailable.")
        return

    print("\n===== PRODUCT FOUND =====")
    print(f"Name: {product['name']}")
    print(f"Brand: {product['brand']}")
    print(f"Barcode: {product['barcode']}")


while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        view_inventory()

    elif choice == "2":
        view_one_item()

    elif choice == "3":
        add_item()

    elif choice == "4":
        update_item()

    elif choice == "5":
        delete_item()

    elif choice =="6":
        find_product()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Option not available yet.")