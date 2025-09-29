''' ASSIGNMENT 2
--------DISCOUNT CALCULATOR------
WRITE A PYTHON PROGRAM THAT CALCULATES THE TOTAL PRICE OF AN ITEMS ENTER BY THE USER,
APPLIES A  DISCOUNT IF THE PRICE EXCEEDS $50, AND THEN DISPLAYS THE DISCOUNTED PRICE.'''
 
 # Assignment 2 - Discount Calculator

# Take input from user
price = float(input("Enter the total price of the item: "))

# Apply discount (10% if price > 50)
discount = 0
if price > 50:
    discount = price * 0.10   # 10% discount

final_price = price - discount

# Show result
print("\n----- BILL -----")
print("Original Price:", price)
print("Discount:", discount)
print("Final Price to Pay:", final_price)