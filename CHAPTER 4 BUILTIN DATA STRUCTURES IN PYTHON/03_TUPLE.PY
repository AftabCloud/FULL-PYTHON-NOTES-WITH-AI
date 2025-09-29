a = () # if we write () phrases these is tuple
print(type(a))
b = (1,)
print(type(b))
c = (1,45,34,787,False,"Rohan",45,"Shivam")
# c[0] = 656 #tuples are immutable
print(type(c))

# TYPES
# type1 Count
no = c.count(45) 
print(no)
# Type 2 Index
i = c.index(787)
print(i)
# concatenation tuple using + operator
tuple1 = (1,2,3)
tuple2 = (4,5,6)
concatenate = tuple1 + tuple2
print(concatenate)
# Repetition triples can be repeated using the * operator
my_tuple = (1,2,3)
repeated = my_tuple*3
print(repeated)

print(len(c))

# slicing
my_tuple = (1,2,3,4,5,6,7)
sliced = my_tuple[1:4]
print(sliced)

# unpacking
my_tuple = (1,2,3)
a, b, c = my_tuple
print(a, b, c)

