# Basic Shopping Cart Program

# Taking input from user
item1 = input("Enter first item name: ") # Input item name
price1 = float(input("Enter price of " + item1 + ": ")) # Input item price

item2 = input("Enter second item name: ") # Input item name
price2 = float(input("Enter price of " + item2 + ": ")) # Input item price

item3 = input("Enter third item name: ") # Input item name
price3 = float(input("Enter price of " + item3 + ": ")) # Input item price

# Calculate total
total = price1 + price2 + price3 # Total price of items

# Apply discount (10% discount if total >= 500)
if total >= 500: # Check if total is eligible for discount
    discount = total * 0.10   # 10% discount
else: # No discount
    discount = 0 # No discount

final_amount = total - discount # Final amount after discount

# Output
print("\n----- BILL -----") # Print bill header
print(item1, ":", price1) # Print first item and price
print(item2, ":", price2) # Print second item and price
print(item3, ":", price3) # Print third item and price
print("Total:", total) # Print total amount
print("Discount:", discount) # Print discount amount
print("Final Amount to Pay:", final_amount) # Print final amount

#item1 = input("ENTER FIRST ITEM NAME: ")
#price1 = float(input("ENTER FIRST ITEM PRICE: "))

item2 = input("ENTER SECOND ITEM NAME: ")
price2 = float(input("ENTER SECOND ITEM PRICE: "))

item3 = input("ENTER THIRD ITEM NAME: ")
price3 = float(input("ENTER THIRD ITEM PRICE: "))

total = price1 + price2 + price3

if total >= 500:
    discount = total * 0.10
else:
    discount = 0 
    final_amount = total - discount

    print("/n------- BILL ---------")
    print(item1, ":", price1)
    print(item2, ":", price2)
    print(item3, ":", price3)
    print("total:", total)
    print("discount:", discount)
    print("final amount to pay:", final_amount)