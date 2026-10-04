from external_api import find_product_by_barcode, find_product_by_name
from unittest.mock import patch, Mock



def test_find_product_by_barcode():
    product = find_product_by_barcode("3017624010701")

    assert product is not None
    assert product["name"] == "Nutella"
    assert product["brand"] == "Ferrero"
    assert product["barcode"] == "3017624010701"



def test_find_product_by_name():
    product = find_product_by_name("Nutella")

    assert product is None or isinstance(product, dict)



def test_find_product_by_barcode_not_found():
    mock_response = Mock()
    mock_response.status_code = 404

    with patch("external_api.requests.get", return_value=mock_response):
        product = find_product_by_barcode("999999999999")

    assert product is None



def test_find_product_by_barcode_api_failure():
    mock_response = Mock()
    mock_response.status_code = 503

    with patch("external_api.requests.get", return_value=mock_response):
        product = find_product_by_barcode("3017624010701")

    assert product is None


def test_find_product_by_name_api_failure():
    mock_response = Mock()
    mock_response.status_code = 503

    with patch("external_api.requests.get", return_value=mock_response):
        product = find_product_by_name("Nutella")

    assert product is None