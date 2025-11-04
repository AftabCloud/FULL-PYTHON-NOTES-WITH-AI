"""
Python Built-in Data Structures
===============================

We have 4 main built-in data structures:
1. List       -> Ordered, Mutable, Allows Duplicates
2. Tuple      -> Ordered, Immutable, Allows Duplicates
3. Set        -> Unordered, Mutable, No Duplicates
4. Dictionary -> Key-Value pairs, Mutable, Keys unique
"""

# ------------------------------
# 1. LIST
# ------------------------------
print("\n=== LIST EXAMPLES ===")

# Definition: List is an ordered, mutable collection that allows duplicate elements
fruits = ["apple", "banana", "cherry"]  # list creation

fruits.append("orange")       # add element at end
fruits.insert(1, "grape")     # insert at index
fruits.extend(["kiwi", "melon"])  # add multiple elements
print("After adding:", fruits)

fruits.remove("banana")       # remove by value
fruits.pop()                  # remove last element
fruits.pop(2)                 # remove element at index
print("After removing:", fruits)

print("Index of apple:", fruits.index("apple"))  # search
print("Count of apple:", fruits.count("apple"))

nums = [3, 1, 4, 1, 5]
nums.sort()                   # ascending sort
print("Sorted:", nums)
nums.sort(reverse=True)       # descending sort
print("Reverse sorted:", nums)
nums.reverse()                # reverse list
print("Reversed:", nums)

copy_list = fruits.copy()     # copy a list
print("Copy of fruits:", copy_list)

print("Slice of fruits:", fruits[0:2])  # slicing


# ------------------------------
# 2. TUPLE
# ------------------------------
print("\n=== TUPLE EXAMPLES ===")

# Definition: Tuple is an ordered, immutable collection that allows duplicates
coords = (10, 20, 30)

print("First element:", coords[0])      # indexing
print("Last element:", coords[-1])      # negative indexing

print("Count of 20:", coords.count(20)) # count occurrences
print("Index of 30:", coords.index(30)) # find index

nested = (1, (2, 3), 4)                 # nested tuple
print("Nested tuple:", nested)

# Convert tuple to list to modify
temp = list(coords)
temp.append(40)
coords = tuple(temp)
print("Modified tuple:", coords)

# ------------------------------
# 3. SET
# ------------------------------
print("\n=== SET EXAMPLES ===")

# Definition: Set is an unordered, mutable collection that stores unique elements
s = {1, 2, 3}

s.add(4)                     # add element
s.update([5, 6])             # add multiple
print("Set after adding:", s)

s.remove(2)                  # remove element (error if missing)
s.discard(7)                 # safe remove
print("Set after removing:", s)

print("Union:", s.union({7, 8}))
print("Intersection:", s.intersection({3, 4, 5}))
print("Difference:", s.difference({1, 5}))
print("Symmetric Difference:", s.symmetric_difference({3, 4}))


# ------------------------------
# 4. DICTIONARY
# ------------------------------
print("\n=== DICTIONARY EXAMPLES ===")

# Definition: Dictionary is a mutable collection of key-value pairs where keys are unique
student = {"name": "Zain", "age": 20, "grade": "A"}

print("Access name:", student["name"])    # access value
print("Access age safely:", student.get("age"))

student["age"] = 21                      # update value
student.update({"city": "Delhi"})        # add new key
print("After update:", student)

student.pop("grade")                     # remove by key
student.popitem()                        # remove last inserted
print("After removals:", student)

print("Keys:", student.keys())           # all keys
print("Values:", student.values())       # all values
print("Items:", student.items())         # key-value pairs

copy_dict = student.copy()               # copy dictionary
print("Copy of student:", copy_dict)


# ------------------------------
# SUMMARY TABLE (printed)
# ------------------------------
print("\n=== SUMMARY ===")
print("""
List       -> Ordered, Mutable, Allows Duplicates
Tuple      -> Ordered, Immutable, Allows Duplicates
Set        -> Unordered, Mutable, No Duplicates
Dictionary -> Mutable, Key-Value pairs, Keys unique
""")