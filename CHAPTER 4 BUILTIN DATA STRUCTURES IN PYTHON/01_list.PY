Freinds = ["Apple", "Orange", 5, 334.06, False, "Akash", "Rohan"] #

print(Freinds[0])
Freinds[0] = "Grapes" # Unlike strings are mutable
print(Freinds[0])
print(Freinds[1:4])

fruits = ["apple", "banana", "cherry"]









# Adding
fruits.append("orange")       # add at end
fruits.insert(1, "grape")     # insert at index
fruits.extend(["kiwi","melon"]) # add multiple

# Removing
fruits.remove("banana")       # removes first occurrence
fruits.pop()                  # removes last element
fruits.pop(2)                 # removes element at index 2
fruits.clear()                # empty the list

# Searching / Counting
print(fruits.index("apple"))  # index of item
print(fruits.count("apple"))  # count occurrences

# Sorting / Reversing
nums = [3, 1, 4, 1, 5]
nums.sort()                   # ascending
nums.sort(reverse=True)       # descending
nums.reverse()                # reverse order

# Copying
copy_list = fruits.copy()

# Slicing
print(fruits[0:2])            # first two items
