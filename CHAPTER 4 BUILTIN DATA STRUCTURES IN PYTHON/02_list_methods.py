Freinds = ["Apple", "Orange", 5, 334.06, False, "Akash", "Rohan"]

print(Freinds)
Freinds.append("ZAIN")
print(Freinds)

l1 = [1,23,2,32,3,43,4]
# l1.sort() # sort = serialwise
# l1.reverse() # l1 is reverse
# l1.insert(3, "ZAIN") #Insert frst position and replacing value
# value = l1.remove(32)
value = l1.pop(3)
print(value)
print(l1) 

cart = ["mouse", "cpu", "monitor", "keyboard", "desktop"]
value = cart.pop() #
print("pop:", cart)
value = cart.append("rahul")
print("list:", cart)
cart.insert(1, "manager")
print(cart)
cart.extend(["naveed"])
print(cart)
cart.remove("mouse")
print(cart)
cart.sort()
print(cart)
#cart.clear()
#print(cart)
cart.count("monitor")
print(cart)