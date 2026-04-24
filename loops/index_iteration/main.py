prices = [29.99, 45.50, 12.75, 38.20]
discounts =[0.10, 0.20, 0.15, 0.05]
for index in range(len(prices)):
    prices[index] -= prices[index] * discounts[index]
    updated_price = prices[index]
    print(f"Updated price for item {index}: ${updated_price:.2f}")