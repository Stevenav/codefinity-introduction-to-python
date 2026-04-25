def apply_discount(prices):
    list_copy = prices.copy()
    discount_threshold = 2.00
    discount=0.10
    for index_value in range(len(list_copy)):
        if list_copy[index_value]>discount_threshold:
            list_copy[index_value] -= list_copy[index_value]*discount
    return list_copy

# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)
print(f"Updated product prices:{updated_prices}")