# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []
for product in products:
    item_details = products[product]
    item_details[0] = float(item_details[0])
    item_details[1] = int(item_details[1])
    total_sales = item_details[0] * item_details[1]
    total_sales_list.append(total_sales)
    print(f"Total sales for {product}: ${total_sales}")
total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
print(f"Total sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")