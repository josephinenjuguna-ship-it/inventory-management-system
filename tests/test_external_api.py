from external_api import find_product_by_barcode, find_product_by_name


def test_find_product_by_barcode():
    product = find_product_by_barcode("3017624010701")

    assert product is not None
    assert product["name"] == "Nutella"
    assert product["brand"] == "Ferrero"
    assert product["barcode"] == "3017624010701"

def test_find_product_by_name():
    product = find_product_by_name("Nutella")

    assert product is None or isinstance(product, dict)