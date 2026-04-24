# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}
discount_threshold = 100
print("Processing")
for item in inventory:
    item_details = inventory.get(item)
    print("Processing",item) 
    while item_details[0]<item_details[1]:
        item_details[0] += item_details[2]
        if item_details[0]>discount_threshold:
            item_details[3] = True
        else:
            item_details[3] =False
print("Processing completed")
    

