'''ASSIGNMENT 1 
----BASIC CALCULATOR----
CREATE A PYTHON PROGRAM THAT ACTS AS A BASIC CALCULATOR
IT SHOULD PROMPT THE USER FOR TWO NUMBERS AND AN OPERATOR (ADD, SUBTRACT, MULTIPLY, DIVIDE)
AND THEN DISPLAY THE RESULT OF THE OPERATION.
'''
# Assignment 1 - Basic Calculator (without if-else)

# Take input from user
num1 = input("Enter first number: ")
operator = input("Enter operator (+, -, *, /): ")
num2 = input("Enter second number: ")

# Evaluate expression
expression = num1 + operator + num2
result = eval(expression)

# Show result
print("Result:", result)
# Note: Using eval can be dangerous if you're taking input from untrusted sources.
# In a real-world application, it's better to use if-else statements to handle operations safely

#OR
# Assignment 1 - Basic Calculator

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Perform calculation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    # To avoid divide by zero error
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Cannot divide by zero."
else:
    result = "Invalid operator!"

# Show result
print("Result:", result)




