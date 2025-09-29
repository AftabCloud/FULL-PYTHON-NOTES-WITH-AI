d = {} # Empty Dictionary
marks = { "Harry": 23,
          "ZAIN": 100,
          "HIPPO": 100,

} 
# print(marks, type(marks))
print(marks)
print(marks ["Harry"])

# Dictionaries are mutable

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