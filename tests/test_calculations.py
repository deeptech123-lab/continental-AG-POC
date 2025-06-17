import pytest
from calculations import calculate_discounted_price


def test_valid_discount():
    assert calculate_discounted_price(100, 20) == 80.0
    assert calculate_discounted_price(250, 0) == 250.0
    assert calculate_discounted_price(500, 100) == 0.0
    assert calculate_discounted_price(99.99, 15) == 84.99


def test_invalid_discount_percent():
    with pytest.raises(ValueError, match="Discount percent must be between 0 and 100"):
        calculate_discounted_price(100, -5)

    with pytest.raises(ValueError, match="Discount percent must be between 0 and 100"):
        calculate_discounted_price(100, 150)


def test_negative_price():
    with pytest.raises(ValueError, match="Original price cannot be negative"):
        calculate_discounted_price(-100, 10)


def test_float_precision():
    assert calculate_discounted_price(199.99, 12.5) == 174.99
