from unittest.mock import patch
import cli


def test_add_item():
    inputs = [
        "Chocolate Bar",
        "DairyLand",
        "100",
        "25",
        "345222333"
    ]

    with patch("builtins.input", side_effect=inputs):
        cli.add_item()

    assert cli.inventory[-1]["name"] == "Chocolate Bar"
    assert cli.inventory[-1]["brand"] == "DairyLand"
    assert cli.inventory[-1]["price"] == 100
    assert cli.inventory[-1]["stock"] == 25
    assert cli.inventory[-1]["barcode"] == "345222333"