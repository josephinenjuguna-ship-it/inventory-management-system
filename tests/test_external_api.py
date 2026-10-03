from unittest.mock import patch, Mock

from external_api import find_product_by_barcode, find_product_by_name

@patch("external_api.requests.get")
def test_find_product_by_barcode(mock_get):
    mock_response = Mock()

    mock_response.status_code = 200

    mock_response.json.return_value = {
        "product": {
            "product_name": "Nutella",
            "brands": "Ferrero",
            "code": "3017624010701"
        }
    }

    mock_get.return_value = mock_response

    product = find_product_by_barcode("3017624010701")

    assert product["name"] == "Nutella"
    assert product["brand"] == "Ferrero"
    assert product["barcode"] == "3017624010701"

@patch("external_api.requests.get")
def test_find_product_by_barcode_not_found(mock_get):
    mock_response = Mock()

    mock_response.status_code = 404

    mock_get.return_value = mock_response

    product = find_product_by_barcode("9999999999999")

    assert product is None

@patch("external_api.requests.get")
def test_find_product_by_barcode_api_unavailable(mock_get):
    mock_response = Mock()

    mock_response.status_code = 503

    mock_get.return_value = mock_response

    product = find_product_by_barcode("3017624010701")

    assert product is None

@patch("external_api.requests.get")
def test_find_product_by_name(mock_get):
    mock_response = Mock()

    mock_response.status_code = 200

    mock_response.json.return_value = {
        "products": [
            {
                "product_name": "Nutella",
                "brands": "Ferrero",
                "code": "3017624010701"
            }
        ]
    }

    mock_get.return_value = mock_response

    product = find_product_by_name("Nutella")

    assert product["name"] == "Nutella"
    assert product["brand"] == "Ferrero"
    assert product["barcode"] == "3017624010701"

@patch("external_api.requests.get")
def test_find_product_by_name_api_unavailable(mock_get):
    mock_response = Mock()

    mock_response.status_code = 503

    mock_get.return_value = mock_response

    product = find_product_by_name("Nutella")

    assert product is None