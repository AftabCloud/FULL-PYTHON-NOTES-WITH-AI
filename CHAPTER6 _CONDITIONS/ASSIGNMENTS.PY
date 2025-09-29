''' MODULE 4: DATA STRUCTURES AND LOGIC BUILDING '''

# ==========================
# ASSIGNMENT 1: CREATE A CONTACT BOOK
# ==========================

# Dictionary to store contacts (name → phone number)
contacts = {}

# Infinite loop to keep showing menu until user exits
while True:
    print("\n--- Contact Book ---")   # Menu header
    print("1. Add Contact")           # Option to add a new contact
    print("2. Search Contact")        # Option to search for a contact
    print("3. Display All Contacts")  # Option to display all saved contacts
    print("4. Exit")                  # Option to quit program
    choice = input("Enter your choice: ")  # Ask user for their choice

    if choice == "1":  # If user chooses Add Contact
        name = input("Enter name: ")             # Take contact name as input
        phone = input("Enter phone number: ")    # Take phone number as input
        contacts[name] = phone                   # Store in dictionary
        print("Contact added successfully!")     # Confirmation message

    elif choice == "2":  # If user chooses Search Contact
        name = input("Enter name to search: ")   # Ask for name to search
        if name in contacts:                     # Check if name exists in dictionary
            print("Phone number of", name, ":", contacts[name])  # Show phone number
        else:
            print("Contact not found.")          # Message if contact missing

    elif choice == "3":  # If user chooses Display All
        print("\nAll Contacts:")                 # Show all saved contacts
        for name, phone in contacts.items():     # Loop through dictionary
            print(name, ":", phone)              # Print each contact

    elif choice == "4":  # If user chooses Exit
        break                                    # Exit the loop → program ends

    else:
        print("Invalid choice! Please try again.")  # If input is not 1-4


# ==========================
# ASSIGNMENT 2: CALCULATE THE INTERSECTION OF TWO SETS
# ==========================

# Take first set input from user (space-separated values → split into list → converted to set)
set1 = set(input("Enter elements of first set (space-separated): ").split())

# Take second set input
set2 = set(input("Enter elements of second set (space-separated): ").split())

# Find intersection (common elements in both sets)
intersection = set1.intersection(set2)
print("Intersection of sets:", intersection)  # Display intersection result


# ==========================
# ASSIGNMENT 3: MANAGE AN INVENTORY SYSTEM
# ==========================

# Dictionary to store inventory (item → quantity)
inventory = {}

# Infinite loop to keep showing menu until user exits
while True:
    print("\n--- Inventory System ---")        # Menu header
    print("1. Add Item")                       # Option to add a new item
    print("2. Update Item Quantity")           # Option to update existing item
    print("3. Display Inventory")              # Option to display all items
    print("4. Exit")                           # Exit option
    choice = input("Enter your choice: ")      # Ask user for choice

    if choice == "1":  # If user chooses Add Item
        item = input("Enter item name: ")      # Ask for item name
        qty = int(input("Enter quantity: "))   # Ask for quantity (convert to int)
        inventory[item] = qty                  # Store item and qty in dictionary
        print("Item added successfully!")      # Confirmation message

    elif choice == "2":  # If user chooses Update Item
        item = input("Enter item name to update: ")  # Ask which item to update
        if item in inventory:                        # Check if item exists
            qty = int(input("Enter new quantity: ")) # New quantity input
            inventory[item] = qty                    # Update dictionary
            print("Quantity updated!")               # Confirmation message
        else:
            print("Item not found.")                 # If item missing

    elif choice == "3":  # If user chooses Display Inventory
        print("\nCurrent Inventory:")                # Show all items
        for item, qty in inventory.items():          # Loop through dictionary
            print(item, ":", qty)                    # Print item with quantity

    elif choice == "4":  # If user chooses Exit
        break                                        # Exit loop → program ends
    else:
        print("Invalid choice!")                     # Wrong input handling


# ==========================
# ASSIGNMENT 4: TUPLE OPERATIONS
# ==========================

# Take input numbers, split by spaces, convert each to int, store as tuple
numbers = tuple(map(int, input("Enter numbers separated by space: ").split()))

print("Tuple:", numbers)         # Show entered tuple
print("Maximum:", max(numbers))  # Find maximum value in tuple
print("Minimum:", min(numbers))  # Find minimum value
print("Sum:", sum(numbers))      # Find sum of all numbers


# ==========================
# ASSIGNMENT 5: UNIQUE WORDS IN A SENTENCE
# ==========================

# Take full sentence input
sentence = input("Enter a sentence: ")

# Split sentence into words, store in set (automatically removes duplicates)
words = set(sentence.split())
print("Unique words:", words)  # Display unique words only
