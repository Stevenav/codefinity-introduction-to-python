# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}
stock_threshold =30
discount_threshold = 100
for item in inventory:
    item_details = inventory.get(item)
    if item_details[0]<stock_threshold:
        print(f"{item} need restocking.")
    else:
        if item_details[0]>discount_threshold:
            print(f"{item} should be sold at the discounted price of {item_details[2]}.")
        else:
            print(f"{item} should be sold at the regular price of {item_details[1]}.")
    
            
        
    