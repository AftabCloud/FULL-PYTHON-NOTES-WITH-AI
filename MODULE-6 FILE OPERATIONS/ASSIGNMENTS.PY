'''-------------------------FILE OPERATIONS--------------------------'''
'''---------------------------ASSIGNMENTS----------------------------'''
# ================================================================
# ASSIGNMENT 1: CREATE A TO-DO LIST MANAGER
# ================================================================

def todo_manager():
    filename = "todo_list.txt"  # File where tasks will be stored

    while True:  # Infinite loop to keep showing menu
        print("\n--- To-Do List Manager ---")  # Menu header
        print("1. Add Task")                   # Option to add a new task
        print("2. View Tasks")                 # Option to view saved tasks
        print("3. Clear Tasks")                # Option to delete all tasks
        print("4. Exit")                       # Option to exit
        choice = input("Enter your choice: ")  # Ask user for choice

        if choice == "1":  # Add Task
            task = input("Enter a new task: ")        # Ask user for task
            with open(filename, "a") as file:         # Open file in append mode
                file.write(task + "\n")               # Write task to file
            print("Task added successfully!")         # Confirm message

        elif choice == "2":  # View Tasks
            try:
                with open(filename, "r") as file:     # Open file in read mode
                    tasks = file.readlines()          # Read all tasks
                    if tasks:                         # If file not empty
                        print("\nYour Tasks:")        # Print header
                        for i, task in enumerate(tasks, 1):  # Loop with numbering
                            print(f"{i}. {task.strip()}")   # Show each task
                    else:
                        print("No tasks found!")      # If file is empty
            except FileNotFoundError:                 # If file not created yet
                print("No task file found. Start adding tasks first.")

        elif choice == "3":  # Clear Tasks
            open(filename, "w").close()               # Open file in write mode (clears it)
            print("All tasks cleared!")               # Confirmation message

        elif choice == "4":  # Exit
            break  # Exit the loop

        else:
            print("Invalid choice! Try again.")  # Wrong input


# ================== Example Input/Output ==================
# Input:
#   1 → Add Task: "Buy groceries"
#   1 → Add Task: "Finish homework"
#   2 → View Tasks
# Output:
#   Your Tasks:
#   1. Buy groceries
#   2. Finish homework
# ================================================================



# ================================================================
# ASSIGNMENT 2: FILE CONTENT SEARCHER
# ================================================================

def file_content_searcher():
    filename = input("Enter filename to search in: ")  # Ask for file name
    word = input("Enter the word to search: ")         # Ask for search word

    try:
        with open(filename, "r") as file:  # Open file
            lines = file.readlines()       # Read all lines

        count = 0  # Counter for occurrences
        print(f"\nSearching for '{word}' in {filename}...\n")
        for line_no, line in enumerate(lines, 1):  # Loop with line number
            if word in line:                       # Check if word in line
                count += line.count(word)          # Count occurrences
                print(f"Line {line_no}: {line.strip()}")  # Show line

        print(f"\nTotal occurrences of '{word}': {count}")  # Final result

    except FileNotFoundError:
        print("File not found!")  # If file missing


# ================== Example Input/Output ==================
# File: notes.txt
# Content:
#   Python is easy.
#   Python is powerful.
#   I love Python!
#
# Input:
#   Enter filename → notes.txt
#   Enter word → Python
# Output:
#   Line 1: Python is easy.
#   Line 2: Python is powerful.
#   Line 3: I love Python!
#   Total occurrences of 'Python': 3
# ================================================================



# ================================================================
# ASSIGNMENT 3: CREATE A SIMPLE FILE COPIER
# ================================================================

def file_copier():
    source = input("Enter source filename: ")         # Ask for source file
    destination = input("Enter destination filename: ")  # Ask for destination file

    try:
        with open(source, "r") as src:   # Open source file in read mode
            content = src.read()         # Read all content

        with open(destination, "w") as dest:  # Open destination in write mode
            dest.write(content)               # Copy content

        print("File copied successfully!")    # Success message

    except FileNotFoundError:
        print("Source file does not exist!")  # Error message


# ================== Example Input/Output ==================
# Source File: hello.txt → "Hello, World!"
# Input:
#   Enter source filename → hello.txt
#   Enter destination filename → copy.txt
# Output:
#   File copied successfully!
# (Now copy.txt will contain "Hello, World!")
# ================================================================



# ================================================================
# ASSIGNMENT 4: CONFIGURATION FILE READER
# ================================================================

def config_reader():
    filename = input("Enter configuration filename: ")  # Ask for config file

    try:
        config = {}  # Dictionary to store key-value pairs
        with open(filename, "r") as file:   # Open file
            for line in file:               # Read line by line
                if "=" in line:             # Check for key=value format
                    key, value = line.strip().split("=", 1)  # Split into key & value
                    config[key] = value     # Store in dictionary

        print("\nConfigurations Loaded:")   # Display all configs
        for key, value in config.items():
            print(f"{key} = {value}")

        # Allow user to search for a specific key
        key_search = input("\nEnter key to retrieve value: ")
        if key_search in config:
            print(f"Value for '{key_search}' is: {config[key_search]}")
        else:
            print("Key not found in configuration.")

    except FileNotFoundError:
        print("Configuration file not found!")  # If missing


# ================== Example Input/Output ==================
# Config File: config.txt
# Content:
#   host=localhost
#   port=5432
#   user=admin
#
# Input:
#   Enter filename → config.txt
#   Enter key → port
# Output:
#   Configurations Loaded:
#   host = localhost
#   port = 5432
#   user = admin
#   Value for 'port' is: 5432
# ================================================================



# ================================================================
# ASSIGNMENT 5: COUNT WORDS AND LINES IN A FILE
# ================================================================

def count_words_lines():
    filename = input("Enter filename: ")  # Ask for file name

    try:
        with open(filename, "r") as file:  # Open file
            lines = file.readlines()       # Read all lines

        num_lines = len(lines)  # Count number of lines
        num_words = sum(len(line.split()) for line in lines)  # Count words

        print(f"\nTotal Lines: {num_lines}")  # Print line count
        print(f"Total Words: {num_words}")    # Print word count

    except FileNotFoundError:
        print("File not found!")  # If file missing


# ================== Example Input/Output ==================
# File: story.txt
# Content:
#   Python is fun.
#   It makes coding easier.
#
# Output:
#   Total Lines: 2
#   Total Words: 6
# ================================================================



# ================================================================
# MAIN MENU (to select assignment)
# ================================================================

while True:
    print("\n--- FILE OPERATIONS ASSIGNMENTS ---")  # Main menu header
    print("1. To-Do List Manager")                  # Run Assignment 1
    print("2. File Content Searcher")               # Run Assignment 2
    print("3. File Copier")                         # Run Assignment 3
    print("4. Config Reader")                       # Run Assignment 4
    print("5. Word & Line Counter")                 # Run Assignment 5
    print("6. Exit")                                # Exit program

    choice = input("Enter your choice: ")  # Ask for choice

    if choice == "1":
        todo_manager()
    elif choice == "2":
        file_content_searcher()
    elif choice == "3":
        file_copier()
    elif choice == "4":
        config_reader()
    elif choice == "5":
        count_words_lines()
    elif choice == "6":
        print("Exiting program. Goodbye!")  # End program
        break
    else:
        print("Invalid choice! Try again.")  # Wrong input handling
