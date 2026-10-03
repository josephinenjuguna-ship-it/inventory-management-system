import requests

def find_product_by_barcode(barcode):
    url = f"https://world.openfoodfacts.org/api/v3/product/{barcode}"

    headers = {
        "User-Agent": "InventoryManagementSystem/1.0"
    }

    response = requests.get(url, headers=headers)


    if response.status_code in (404, 503):
        return None

    response.raise_for_status()

    data = response.json()
    product = data["product"]

    return {
        "name": product.get("product_name", "Unknown"),
        "brand": product.get("brands", "Unknown"),
        "barcode": product.get("code", barcode)
    }


def find_product_by_name(name):
    url = "https://world.openfoodfacts.org/cgi/search.pl"

    params = {
        "search_terms": name,
        "search_simple": 1,
        "action": "process",
        "json": 1,
        "page_size": 1
    }

    headers = {
        "User-Agent": "InventoryManagementSystem/1.0"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers
    )


    if response.status_code == 503:
        return None

    response.raise_for_status()

    data = response.json()

    products = data.get("products", [])

   
    if not products:
        return None

    product = products[0]

    return {
        "name": product.get("product_name", "Unknown"),
        "brand": product.get("brands", "Unknown"),
        "barcode": product.get("code", "Unknown")
    }