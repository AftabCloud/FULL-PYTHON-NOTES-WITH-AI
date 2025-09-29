s = {2,3,5} #curly bracketes with inside called as sets

e = set() #don't use s = {} as it is empty dictonary can't say the empty set
s = {3, 5, 32, 45, 5, 5, 5,} #in sets elements are not repeated it 5 treat as only one
print(s)

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