# A VARIABLE IS A PLACEHOLDER FOR INFORMATION YOU WANT 
# PYTHON TO RECALL LATER IN THE CODING PROCESS 
# WHEN YOU NEED TO COMPLETE AN ACTION
A = 1 # THIS VARIABLE A IS ASSIGNED THE VALUE 1

B = 2 # THIS VARIABLE B IS ASSIGNED THE VALUE 2

name = "ZAIN AFTAB" # THIS NAME VARIABLE IS ASSIGNED THE VALUE "ZAIN AFTAB"
print(name) # PRINT FUNCTION DISPLAYS THE VALUE OF THE VARIABLE NAME
print(A + B) # PRINT FUNCTION DISPLAYS THE VALUE OF THE EXPRESSION A + B

# https://chatgpt.com/s/t_68d4fef7efb48191a7f3497a5f715f80
# ==============================
# VARIABLES IN PYTHON - BASICS
# ==============================

# A variable is like a container(place holder) that stores a data value
# so you can use it later in your program.
# In Python, you don’t need to declare the type of variable explicitly.
# The type is automatically decided based on the value assigned.
# types of varibles: 1.integer(numbers),2.float(decimal float),3.string(charecters).
#4.boolean variable, 5.nontype
# ------------------------------
# Example 1: Integer variable
# ------------------------------
age = 21  

# Here, 'age' is the variable name and 21 is the integer value stored in it.
print("Age:", age)  # Prints the value stored in variable 'age'

# ------------------------------
# Example 2: Float variable
# ------------------------------
price = 99.99  # 'price' is a variable storing a decimal (float) value
print("Price:", price)  # Prints the value stored in variable 'price'

# ------------------------------
# Example 3: String variable
# ------------------------------
name = "Zain Aftab"  # 'name' stores a sequence of characters (string)
print("Name:", name)  # Prints the value stored in variable 'name'

# ------------------------------
# Example 4: Boolean variable
# ------------------------------
is_student = True  # 'is_student' stores a True/False value (Boolean type)
print("Is Student:", is_student)  # Prints whether the student status is True or False

# ------------------------------
# Example 5: None type variable
# ------------------------------
empty_value = None  # 'None' represents no value or null
print("Empty Value:", empty_value)  # Prints None

# ------------------------------
# Checking variable types
# ------------------------------
# We can use the built-in type() function to check the data type of a variable
print("Type of age:", type(age))            # int
print("Type of price:", type(price))        # float
print("Type of name:", type(name))          # str
print("Type of is_student:", type(is_student))  # bool
print("Type of empty_value:", type(empty_value)) # NoneType

# ------------------------------
# Rules for variable names
# ------------------------------
# 1. Variable names must start with a letter or underscore (_), not with a number.
# 2. They can contain letters, numbers, and underscores.
# 3. They are case-sensitive (myVar and myvar are different).
# 4. Use meaningful names for readability.

# Valid examples:
student_name = "Ali"
_student_age = 20
total_marks1 = 450

# Invalid examples (will cause errors if uncommented):
# 1student = 10    # cannot start with a number
# total-marks = 90 # cannot use hyphen
# class = "Python" # cannot use reserved keywords

# ------------------------------
# Interview Tip:
# ------------------------------
# A variable is simply a name that refers to a memory location where data is stored.
# Python is dynamically typed → you don’t need to declare the type, it is inferred automatically.


 # https://chatgpt.com/s/t_68d503d7e890819189193c765cd5ef62 Python Variable Interview Questions / Answers
# ==============================
# VARIABLES IN PYTHON - DEMO FILE
# ==============================

# Q1: What is a variabl in python?
# A variable is like a container(place holder) that stores a data value.
# so you can use it later in your program.
# In Python, you don’t need to declare the type of variable explicitly.
# The type is automatically decided based on the value assigned.
# types of varibles: 1.integer(numbers),2.float(decimal float),3.string(characters).
#4.boolean variable, 5.nontype.
x = 10  # Here, 'x' is a variable storing the integer 10
name = "Zain"  # 'name' stores a string value
is_active = True  # 'is_active' stores a boolean value

# Q2: How do you declare variables in Python?
# Python is dynamically typed → no need to specify data type
a = 5          # integer
b = "Hello"    # string
c = 3.14       # float

# Q3: Rules for variable naming
# Variable names must start with a letter or underscore (_), not with a number.
# 2. They can contain letters, numbers, and underscores.
# 3. They are case-sensitive (myVar and myvar are different).
# 4. Use meaningful names for readability.
# Valid examples
my_var = 100
_var = "underscore start"
var123 = "numbers allowed"
Name = "Case-sensitive example"

# ❌ Invalid examples (will cause error if used)
# 123var = 50      # cannot start with number
# my-var = 20      # hyphen not allowed
# class = "oops"   # reserved keyword

# Q4: Global vs Local variables
global_var = "I am global"  # defined outside any function

def test_scope():
    local_var = "I am local"  # exists only inside this function
    print(local_var)  # prints local variable
    print(global_var) # can access global variable inside function

test_scope()
# print(local_var)  # ❌ would cause error (not accessible outside function)

# Q5: Constants in Python
# By convention, we write constants in UPPERCASE
PI = 3.1416
MAX_USERS = 100

# Q6: Dynamic typing
x = 10       # int
print(type(x))  # <class 'int'>
x = "Zain"   # now it's a string
print(type(x))  # <class 'str'>

# Q7: Mutable vs Immutable variables
# Immutable → cannot change (int, float, str, tuple)
num = 100
# num[0] = 5  # ❌ not allowed

text = "hello"
# text[0] = "H"  # ❌ not allowed

# Mutable → can change (list, dict, set)
my_list = [1, 2, 3]
my_list[0] = 10  # ✅ allowed
print(my_list)

# Q8: Reserved keywords
# Keywords like if, else, for, class cannot be used as variables
# Example (invalid):
# if = 5  # ❌ error

# Q9: Deleting a variable
temp = 500
print(temp)  # prints 500
del temp     # deletes the variable from memory
# print(temp)  # ❌ NameError (no longer exists)

# Q10: Variable Scope (LEGB Rule)
# L = Local, E = Enclosing, G = Global, B = Built-in

var = "global variable"  # Global scope

def outer():
    var = "enclosing variable"  # Enclosing scope

    def inner():
        var = "local variable"  # Local scope
        print("Inside inner:", var)

    inner()
    print("Inside outer:", var)

outer()
print("Outside all:", var)

