# ''' -------ASSIGNMENTS---------- 
# ASSIGNMENT 1: CREATE A BASIC CALCULATOR USING FUNCTIONS
# OBJECTIVE: WRITE A PYTHON PROGRAM USING FUNCTIONS TO PERFORM BASIC ARITHMETIC OPERATIONS (ADDITION, SUBSTRACTION, MULTIPLICATION, DIVISION)
# TASKS:
# 1. DEFINE A SEPARATE FUNCTION FOR EACH OPERATION.
# 2. ACCEPT TWO NUMBERS AND AN OPERATOR FROM THE USER.
# 3. CALL THE APPROPRIATE FUNCTION BASED ON THE OPERATOR.
# ''' 
# Assignment 1: Basic Calculator using functions
# Function to add two numbers
# def add(a, b):
#     return a + b
# # Function to subtract two numbers
# def subtract(a, b):
#     return a - b
# # Function to multiply two numbers
# def multiply(a, b):
#     return a * b
# # Function to divide two numbers
# def divide(a, b):
#     if b == 0:      # Check for divide by zero
#         return "Cannot divide by zero!"
#     else:
#         return a / b
# # Get user input
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operator = input("Enter operator (+, -, *, /): ")
# # Call the matching function
# if operator == '+':
#     print("Result:", add(num1, num2))
# elif operator == '-':
#     print("Result:", subtract(num1, num2))
# elif operator == '*':
#     print("Result:", multiply(num1, num2))
# elif operator == '/':
#     print("Result:", divide(num1, num2))
# else:
#     print("Invalid operator")
# # Enter first number: 10
# # Enter second number: 20
# # Enter operator (+, -, *, /): +
# # Result: 30.0
# # Do you want to calculate again? (yes/no):

# ''' ----------------ASSIGNMENT-2---------------
# ASSIGNMENT-2: IMPLEMENT A BANK ACCOUNT  CLASS
# OBJECTIVE: CREATE A BANKACCOUNT CLASS TO MANAGE USER ACCOUNTS.
# TASKS: 
# 1. DEFINE ATTRIBUTES FOR ACCOUNT HOLDER NAME AND BALANCE.
# 2. IMPLEMENT METHODS FOR DEPOSIT, WITHDRAWL, AND DISPLAYING THE ACCOUNT BALANCE.
# 3. TEST THE CLASS BY CREATING A BANK ACCOUNT AND PERFORMING TRANSACTIONS.
# '''
# # Assignment 2: Bank Account Class
# # Create a class to manage bank accounts
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name              # Store account holder name
#         self.balance = balance        # Store the starting balance

#     def deposit(self, amount):
#         self.balance += amount        # Add money to the balance
#         print(f"Deposited {amount}. New balance is {self.balance}.")

#     def withdraw(self, amount):
#         if amount > self.balance:     # Check if there's enough money
#             print("Insufficient funds.")
#         else:
#             self.balance -= amount    # Subtract the amount
#             print(f"Withdrew {amount}. New balance is {self.balance}.")

#     def display(self):
#         print(f"Account Holder: {self.name}")
#         print(f"Balance: {self.balance}")

# # Create an account and try deposit/withdraw
# account = BankAccount("Rahul", 500)
# account.display()
# account.deposit(200)
# account.withdraw(100)
# account.display()

# # Account Holder: Rahul
# # Balance: 500
# # Deposited 200. New balance is 700.
# # Withdrew 100. New balance is 600.
# # Account Holder: Rahul
# # Balance: 600
# # Do you want to do another transaction? (yes/no): 


# ''' --------------------ASSIGNMENT -3------------------------------
# ASSIGNMENT-3: EMPLOYEE MANAGEMENT SYSTEM 
# OBJECTIVE: CREATE AN EMPLOYEE CLASS TO MANAGE EMPLOYEE DATA.
# TASKS:
# 1.DEFINE ATTRIBUTES FOR NAME, ID, AND SALARY.
# 2. IMPLEMENT A METHOD TO DISPLAY EMPLOYEE DETAILS.
# 3. CREATE MULTIPLE EMPLOYEE OBJECTS AND DISPLAY THEIR DETAILS.
# '''
# # Assignment 3: Employee Management System

# # Create an Employee class
# class Employee:
#     def __init__(self, name, emp_id, salary):
#         self.name = name           # Employee name
#         self.emp_id = emp_id       # Employee ID
#         self.salary = salary       # Employee salary

#     def display_details(self):
#         print(f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}")

# # Make some Employee objects and display info
# emp1 = Employee("Anil", 101, 25000)
# emp2 = Employee("Priya", 102, 27000)
# emp3 = Employee("Suresh", 103, 30000)

# emp1.display_details()
# emp2.display_details()
# emp3.display_details()

# # Employee 1:
# # Name: Anil, ID: 101, Salary: 25000
# # Employee 2:
# # Name: Priya, ID: 102, Salary: 27000
# # Employee 3:
# # Name: Suresh, ID: 103, Salary: 30000
# # Do you want to display employees again? (yes/no): 

# '''------------ASSIGNMENT-4-------------
# OBJECTIVEl: DEVELOP A PROGRAM TO STORE AND MANAGE STUDENT PERFORMANCE USING OOP.
# TASKS:
# 1. CREATE A STUDENT CLASS WITH ATTRIBUTES FOR NAME, AGE, AND GRADES.
# 2. IMPLEMENT METHODS TO CALCULATE AND DISPLAY THE AVERAGE GRADE.
# 3. ALLOW THE USER TO ADD MULTIPLE STUDENTS AND DISPLAY THEIR AVERAGE GRADES.
# '''
# # Assignment 4: Student Performance Management

# Create a Student class
# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name                   # Student name
#         self.age = age                     # Student age
#         self.grades = grades               # List of grades

#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)   # Average grade

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, Average Grade: {self.average_grade()}")

# # Add some students and display their averages
# students = []
# students.append(Student("Amit", 20, [85, 90, 80]))
# students.append(Student("Neha", 21, [75, 80, 70]))

# for student in students:
#     student.display()

# OUTPUT
# # Student 1:
# # Name: Amit, Age: 20, Average Grade: 85.0
# # Student 2:
# # Name: Neha, Age: 21, Average Grade: 75.0
# # Do you want to view student averages again? (yes/no): 



# '''------------------ASSIGNMENT-5---------------------
# ASSIGNMENT- 5: BOOKSTORE INVENTORY SYSTEM
# OBJECTIVE: BUILD A  BOOKSTORE CLASS TO MANAGE BOOK INVENTORY.
# TASKS: 
# 1. DEFINE ATTRIBUTES FOR BOOK TITLE, AUTHOR, AND QUANTITY.
# 2. IMPLEMENT METHODS TO ADD BOOKS, SELL BOOKS, AND DISPLAY INVENTORY.
# 3. TEST THE SYSTEM BY ADDING AND SELLING BOOKS.
# '''
# # Assignment 5: Bookstore Inventory System
class Book:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity

class Bookstore:
    def __init__(self):
        self.inventory = []     # List to hold books

    def add_book(self, title, author, quantity):
        self.inventory.append(Book(title, author, quantity))
        print(f"Added {quantity} copies of '{title}'.")

    def sell_book(self, title, amount):
        for book in self.inventory:
            if book.title == title:
                if book.quantity >= amount:
                    book.quantity -= amount
                    print(f"Sold {amount} copies of '{title}'.")
                else:
                    print(f"Not enough copies to sell for '{title}'.")
                break
        else:
            print(f"Book '{title}' not found.")

    def display_inventory(self):
        print("Bookstore Inventory:")
        for book in self.inventory:
            print(f"{book.title} by {book.author} - {book.quantity} copies left")

# Testing bookstore
store = Bookstore()
store.add_book("Python 101", "Guido", 5)
store.add_book("AI Basics", "Andrew", 3)
store.sell_book("Python 101", 2)
store.display_inventory()


# # Output:
# # text
# # Added 5 copies of 'Python 101'.
# # Added 3 copies of 'AI Basics'.
# # Sold 2 copies of 'Python 101'.
# # Bookstore Inventory:
# # Python 101 by Guido - 3 copies left
# # AI Basics by Andrew - 3 copies left