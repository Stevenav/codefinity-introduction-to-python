grocery_inventory = {"Milk":("Dairy",3.50,8), "Eggs":("Dairy",5.50,30), "Bread":("Bakery",2.99,15),"Apples":("Produce",1.50,50)}
egg_details = grocery_inventory.get("Eggs")
print(egg_details)
if egg_details[2]>5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory.update({"Eggs":("Dairy",4.50,30)})
else:
    print("The price of Eggs is reasonable")
grocery_inventory.update({"Tomatoes":("Produce",1.20,30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
print(grocery_inventory)
milk_details = grocery_inventory.get("Milk")
if milk_details[2]<10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory.update({"Milk":("Dairy",3.50, 28)})
else:
    print("Milk has sufficient stock.")
apple_details=grocery_inventory.get("Apples")
if apple_details[1]>2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
print("updated inventory:",grocery_inventory)
    