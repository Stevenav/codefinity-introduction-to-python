def apply_discount(prices):
    list_copy = prices.copy()
    print(list_copy)
    discount_threshold =2.00
    discount=.10
    for item in list_copy:
        if list_copy[price] > discount_threshold:
            list_copy -= list_copy[price] * discount
    print(list_copy)
    return list_copy

# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)