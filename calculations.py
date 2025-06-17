def calculate_discounted_price(original_price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters
    ----------
    original_price : float
        The original price of the item.
    discount_percent : float
        The discount percentage to apply.

    Returns
    -------
    float
        The final price after discount.

    Raises
    ------
    ValueError
        If original_price is negative or discount_percent is not between 0 and 100.
    """
    if original_price < 0:
        raise ValueError("Original price cannot be negative.")
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount percent must be between 0 and 100.")

    discount_amount = (discount_percent / 100) * original_price
    return round(original_price - discount_amount, 2)
