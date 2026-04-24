produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries =[]
groceries.append(produce)
groceries.append(dairy)
print(groceries)
for section in groceries:
    for item in section:
        print("Item name:", item)