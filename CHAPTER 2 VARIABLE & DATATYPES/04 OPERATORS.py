# Arithematic Operators
a = 34
b = 4 
c = a + b
print(c)

# Assignment Operators
a = 4-2 # assign 4-2 in a
print(a)
b = 6 
b += 3 # Increment the value of b by 3 and then assign it to b
# b -= 3 # decrement the value of b by 3 and then assign it to b
# b *= 3 # Multiply the value of b by 3 and then assign it to b
# b /= 3 # Divide the value of b by 3 and then assign it to b
print(b)


# Comparsion Operators
d = 5<4  #false
# d = 5>4 true
# d = 5>=4 true
# d= 5<=4 false
# d= 5!=7 True
# d = 5!=5 True
d = 5==5
print(d)

# Logical Operators
e  = True or False

# Truth table of 'or'
print("True or False is", True or False)
print("True or True is", True or True )
print("False or True is", False or  True)
print("False or False is", False or False)
print(e)

# truth table of 'and'
print("True and True is", True and True )
print("False and True is", False and  True)
print("False and False is", False and False)
print("True and False is", True and False)
# true ko bhi false kahdena
print(not(True))

 

# https://chatgpt.com/s/t_68d50253f3908191950a38ef7eca2d2b Operators in Python
# ==============================
# Python Operators - Beginner Guide
# ==============================
# Operators are special symbols in Python used to perform operations on values/variables

# Operands are the values/variables on which operators work

# Example: In "a + b", '+' is the operator, and a, b are operands

# ----------------------------------
# 1. Arithmetic Operators
# ----------------------------------

a = 10  # integer value
b = 3   # another integer value

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.333...
print(a // b)  # Floor Division → 3 (removes decimal part)
print(a % b)   # Modulus → 1 (remainder)
print(a ** b)  # Exponent → 1000 (10^3)

# ----------------------------------
# 2. Comparison (Relational) Operators
# ----------------------------------

x = 5
y = 10

print(x == y)   # Equal → False
print(x != y)   # Not Equal → True
print(x > y)    # Greater than → False
print(x < y)    # Less than → True
print(x >= y)   # Greater or equal → False
print(x <= y)   # Less or equal → True

# ----------------------------------
# 3. Assignment Operators
# ----------------------------------

z = 10   # assign 10 to z
z += 5   # same as z = z + 5 → 15
z -= 3   # same as z = z - 3 → 12
z *= 2   # same as z = z * 2 → 24
z /= 4   # same as z = z / 4 → 6.0
z //= 2  # same as z = z // 2 → 3
z %= 2   # same as z = z % 2 → 1
z **= 3  # same as z = z ** 3 → 1

# ----------------------------------
# 4. Logical Operators
# ----------------------------------

a = True
b = False

print(a and b)  # AND → False
print(a or b)   # OR → True
print(not a)    # NOT → False

# ----------------------------------
# 5. Bitwise Operators (work on binary numbers)
# ----------------------------------

x = 6   # binary: 110
y = 3   # binary: 011

print(x & y)   # AND → 2 (010)
print(x | y)   # OR  → 7 (111)
print(x ^ y)   # XOR → 5 (101)
print(~x)      # NOT → -7
print(x << 1)  # Left shift → 12 (binary shift left)
print(x >> 1)  # Right shift → 3 (binary shift right)

# ----------------------------------
# 6. Membership Operators
# ----------------------------------

nums = [1, 2, 3, 4]

print(2 in nums)      # True (2 exists in list)
print(10 not in nums) # True (10 does not exist)

# ----------------------------------
# 7. Identity Operators
# ----------------------------------

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)      # False (different memory locations)
print(a == b)      # True (values are same)
print(a is c)      # True (same object in memory)
print(a is not b)  # True (not same object)
# ==============================
# END OF FILE
# ==============================

# https://chatgpt.com/s/t_68d5027d4b048191963408e6d16e1bf2 INTERVIEW QUESTIONS ON OPERATORS
"""
Python Operators - Interview Questions & Answers
Beginner-friendly explanations with one-line comments and examples
"""

# ===============================
# Q1. Difference between == and is
# ===============================

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True → values are equal
print(a is b)  # False → different objects in memory
print(a is c)  # True  → same memory reference


# ===============================
# Q2. Difference between / and //
# ===============================

print(7 / 2)   # 3.5 → normal division (float result)
print(7 // 2)  # 3   → floor division (removes decimal part)


# ===============================
# Q3. Logical Operators (and, or, not)
# ===============================

x, y = True, False
print(x and y)  # False → both must be True
print(x or y)   # True  → at least one must be True
print(not x)    # False → reverses value


# ===============================
# Q4. Difference between != and is not
# ===============================

m = [1, 2]
n = [1, 2]

print(m != n)     # False → values are equal
print(m is not n) # True  → different objects in memory


# ===============================
# Q5. Operator Precedence
# ===============================

result = 10 + 2 * 3   # * has higher precedence than +
print(result)         # 16

# Precedence order (high → low):
# () → ** → * / // % → + - → < > == → not → and → or


# ===============================
# Q6. Swap numbers without temp variable
# ===============================

a, b = 10, 20
a, b = b, a   # Pythonic way
print(a, b)   # 20, 10


# ===============================
# Q7. Membership Operators (in, not in)
# ===============================

nums = [1, 2, 3]
print(2 in nums)       # True → 2 is in the list
print(5 not in nums)   # True → 5 is not in the list


# ===============================
# Q8. Bitwise vs Logical Operators
# ===============================

print(6 & 3)           # 2 → bitwise AND (110 & 011 = 010)
print(True and False)  # False → logical AND


# ===============================
# Q9. Chained Comparison
# ===============================

x = 10
print(5 < x < 20)  # True → shorthand for (5 < x and x < 20)


# ===============================
# Q10. Augmented Assignment Operators
# ===============================

x = 10
x += 5   # same as x = x + 5
x *= 2   # same as x = x * 2
print(x) # 30

