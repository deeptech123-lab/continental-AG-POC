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
    # Calculating discount
    discount_amount = (discount_percent / 100) * original_price
    print("Calculated discount")
    return round(original_price - discount_amount, 2)

def apply_tax(price, tax_rate_percent):
    return round(price + (price * tax_rate_percent / 100), 2)

def get_final_price(original_price, discount_percent, tax_rate_percent):
    price_after_discount = calculate_discounted_price(original_price, discount_percent)
    final_price = apply_tax(price_after_discount, tax_rate_percent)
    return final_price
