a = 1 # a is a integer

b = 5.22 # b is a Floating point

c = "ZAIN AFTAB" #c is a string

d = False # d is a Boolean variable
 
e = None # e is a none type variable

# https://chatgpt.com/s/t_68d4ffc9cbd081919b768f2f136a2b88 # Data types in Python
''''''
# ---- NUMERIC TYPES ----
# Integer (int): whole numbers without a decimal point
age = 25                     # int: 25 is a whole number

# Float (float): numbers with decimal points
price = 99.99                # float: has fractional part

# Complex (complex): numbers with a real and imaginary part
z = 3 + 5j                   # complex: 3 is real part, 5j is imaginary part

# ---- TEXT TYPE ----
# String (str): sequence of characters (text), use quotes
name = "Zain Aftab"         # str: store names, sentences, etc.

# ---- BOOLEAN TYPE ----
# Boolean (bool): True or False values, often used for conditions
is_student = True            # bool: only True or False
has_paid = False             # bool: represents yes/no, on/off

# ---- SEQUENCE TYPES ----
# List (list): ordered, changeable, allows duplicates
fruits = ["apple", "banana", "cherry"]   # list: use []

# Tuple (tuple): ordered, but immutable (cannot change), allows duplicates
colors = ("red", "green", "blue")        # tuple: use ()

# Range (range): represents a sequence of numbers (commonly used in loops)
numbers_range = range(0, 5)   # range: 0,1,2,3,4

# ---- SET TYPES ----
# Set (set): unordered collection of unique items (duplicates removed)
unique_nums = {1, 2, 3, 2}    # set: duplicate 2 will be stored only once

# Frozenset (frozenset): immutable set (cannot add/remove items)
frozen = frozenset([1, 2, 3])

# ---- MAPPING TYPE ----
# Dictionary (dict): collection of key:value pairs (like a real-world dictionary)
student = {"name": "Zain", "age": 21, "is_student": True}  # dict: use {}

# ---- NONE TYPE ----
# NoneType (None): represents the absence of a value
x = None                     # None: value not set or intentionally empty

# ---- SIMPLE USAGE EXAMPLES ----
# Print values and their types using the built-in type() function
print("--- Values and their types ---")
print("age ->", age, "type:", type(age))
print("price ->", price, "type:", type(price))
print("z ->", z, "type:", type(z))
print("name ->", name, "type:", type(name))
print("is_student ->", is_student, "type:", type(is_student))
print("fruits ->", fruits, "type:", type(fruits))
print("colors ->", colors, "type:", type(colors))
print("numbers_range ->", list(numbers_range), "type:", type(numbers_range))
print("unique_nums ->", unique_nums, "type:", type(unique_nums))
print("frozen ->", frozen, "type:", type(frozen))
print("student ->", student, "type:", type(student))
print("x ->", x, "type:", type(x))

# ---- COMMON OPERATIONS (quick cheatsheet) ----
# 1) Convert types: int(), float(), str()
num_str = "10"                # string that looks like a number
num_int = int(num_str)         # convert string to integer
num_float = float(num_str)     # convert string to float
print("\n-- Conversions --")
print(num_str, "->", num_int, type(num_int))
print(num_str, "->", num_float, type(num_float))

# 2) String operations: concatenation and f-strings
greeting = "Hello"
who = "Zain"
message = greeting + ", " + who + "!"        # concatenation using +
message_f = f"{greeting}, {who}!"             # f-string (recommended)
print("\n-- Strings --")
print(message)
print(message_f)

# 3) List operations: add, remove, access by index
print("\n-- Lists --")
fruits.append("orange")       # add an item
print("after append:", fruits)
print("first fruit:", fruits[0])  # index starts at 0
fruits.remove("banana")       # remove an item by value
print("after remove:", fruits)

# 4) Tuple: immutable (no append/remove), but you can access by index
print("\n-- Tuples --")
print("colors[1]:", colors[1])

# 5) Set: fast membership test, unique elements
print("\n-- Sets --")
print("unique_nums contains 2?", 2 in unique_nums)
unique_nums.add(4)              # add a new unique item
print("after add:", unique_nums)

# 6) Dict: access by key, add new key:value
print("\n-- Dicts --")
print("student name:", student["name"])  # get value using key
student["grade"] = "A+"       # add new key:value pair
print("after adding grade:", student)

# 7) None: often used as a default value or placeholder
print("\n-- NoneType --")
def find_user(user_list, name_to_find):
    # function returns a dict (user) if found, otherwise None
    for u in user_list:
        if u.get("name") == name_to_find:
            return u
    return None

users = [{"name": "Zain"}, {"name": "Aisha"}]
res = find_user(users, "Ali")
print("found user:", res)  # will print None if not found

# ---- SHORT QUIZ (try to answer before running) ----
# 1. Which type would you use to store the age of a person? (int)
# 2. Which type would you use to store a list of books? (list)
# 3. What does None represent? (no value / empty)
# 4. Can you change a tuple after creating it? (No, tuples are immutable)

print("\n--- Quiz answers: 1=int, 2=list, 3=None means no value, 4=No (immutable) ---")

# ---- END ----
# Save and run this file to experiment: change values, add prints, and play with types!

# https://chatgpt.com/s/t_68d504df305881918615f97e7f695eac Data Types Interview Questions / Answers

''''''
#PYTHON DATA TYPES - INTERVIEW QUESTIONS & ANSWERS
# This file contains common interview questions on Python data types
# with beginner-friendly explanations and examples.
'''
'''
# ============================
# Q1. What are the built-in data types in Python?
# ============================

# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Text Type: str
# Set Types: set, frozenset
# Mapping Type: dict
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview
# None Type: NoneType

# Example:
num = 10        # int
pi = 3.14       # float
z = 2 + 3j      # complex
name = "Alice"  # str
fruits = ["apple", "banana"]  # list
colors = ("red", "blue")      # tuple
nums = {1, 2, 3}              # set
student = {"id": 1, "age": 20} # dict
flag = True   # bool
data = b"abc" # bytes


# ============================
# Q2. Difference between mutable and immutable data types?
# ============================

# Mutable -> can be changed (list, dict, set)
# Immutable -> cannot be changed (int, float, str, tuple)

x = [1,2,3]   # list is mutable
x[0] = 100    # allowed

y = "hello"   # string is immutable
# y[0] = "H"  # ❌ not allowed


# ============================
# Q3. Difference between list and tuple?
# ============================

# List -> mutable, slower, uses []
# Tuple -> immutable, faster, uses ()

my_list = [1,2,3]
my_tuple = (1,2,3)


# ============================
# Q4. Difference between set and list?
# ============================

# List -> ordered, allows duplicates
# Set -> unordered, unique only

my_list = [1,2,2,3]
my_set = {1,2,2,3}
print(my_list) # [1,2,2,3]
print(my_set)  # {1,2,3}


# ============================
# Q5. Difference between str, bytes, and bytearray?
# ============================

s = "hello"                  # str (text)
b = b"hello"                 # bytes (immutable binary)
ba = bytearray(b"hello")     # bytearray (mutable binary)


# ============================
# Q6. Difference between isinstance() and type()?
# ============================

x = 10
print(type(x))            # <class 'int'>
print(isinstance(x, int)) # True

# ============================
# Q7. Difference between None, False, and 0?
# ============================

print(None == False) # False
print(False == 0)    # True
print(None == 0)     # False


# ============================
# Q8. What is a dictionary in Python?
# ============================

# dict = key-value pairs, unordered, mutable
student = {"name": "Zain", "age": 21}
print(student["name"])  # Zain


# ============================
# Q9. Difference between shallow copy and deep copy?
# ============================

import copy
a = [[1,2],[3,4]]
shallow = copy.copy(a)       # shallow copy
deep = copy.deepcopy(a)      # deep copy


# ============================
# Q10. How to check the type of a variable?
# ============================

x = [1,2,3]
print(type(x))             # <class 'list'>
print(isinstance(x, list)) # True


# ============================
# Q11. Difference between frozenset and set?
# ============================

s = {1,2,3}                       # set (mutable)
fs = frozenset([1,2,3])           # frozenset (immutable)


# ============================
# Q12. Difference between range() and xrange()?
# ============================

# In Python 3 -> only range() exists (like xrange in Python 2)
r = range(5)
print(list(r))  # [0,1,2,3,4]
 