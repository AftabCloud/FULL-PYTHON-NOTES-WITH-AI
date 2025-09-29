import datetime

# Function to log actions
def log_action(action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("user_log.txt", "a") as log_file:
        log_file.write(f"{timestamp} – {action}\n")

# Function to display log content
def display_log():
    try:
        with open("user_log.txt", "r") as log_file:
            content = log_file.read()
            print("\nLog Content:\n", content if content else "No logs yet.")
    except FileNotFoundError:
        print("Log file does not exist. No actions have been logged yet.")

# Main program
while True:
    print("\nChoose an action:")
    print("1. Login")
    print("2. Logout")
    print("3. Perform task")
    print("4. View log")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        log_action("User logged in")
        print("Logged in successfully.")
    elif choice == "2":
        log_action("User logged out")
        print("Logged out successfully.")
    elif choice == "3":
        task = input("Enter task description: ")
        log_action(f"User performed task: {task}")
        print("Task logged successfully.")
    elif choice == "4":
        display_log()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
