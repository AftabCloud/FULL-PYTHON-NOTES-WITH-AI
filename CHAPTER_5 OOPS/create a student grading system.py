'''USECASE: CREATE A STUDENT GRADING SYSTEM 
OBJECTIVE: Develop a python program using functions and oop to manage student details and calculate their average grade. The programe should. 
1.	Accept student details(name, age , grades).
2.	Calculate and display the average grade for each student.
3.	Display a summary of all students and their average grades.

 CODE: https://chatgpt.com/s/t_68d7c19405d081919fe8d73ec099fbfa
 
 🛠 Requirements

Accept student details → name, age, grades.

Calculate average grade for each student.

Display a summary of all students.

✅ Full Python Code
# 🎯 Student Grading System using OOP + Functions

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    # Function to calculate average
    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    # Function to display student details
    def display_details(self):
        avg = self.calculate_average()
        print(f"Name: {self.name}, Age: {self.age}, Average Grade: {avg:.2f}")


# Function to display summary of all students
def display_summary(students_list):
    print("\n📌 Student Summary Report:")
    for student in students_list:
        student.display_details()


# ---------------- MAIN PROGRAM ----------------
students = []  # list to store student objects

while True:
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    
    # Accept grades as comma separated values
    grades = list(map(int, input("Enter grades separated by space: ").split()))
    
    # Create Student object
    student = Student(name, age, grades)
    students.append(student)
    
    choice = input("Do you want to add another student? (yes/no): ").lower()
    if choice == "no":
        break

# Display report
display_summary(students)

🖥 Example Run
Enter Student Name: Zaiin
Enter Student Age: 20
Enter grades separated by space: 85 90 78
Do you want to add another student? (yes/no): yes

Enter Student Name: Shaik
Enter Student Age: 22
Enter grades separated by space: 70 80 90
Do you want to add another student? (yes/no): no

📌 Student Summary Report:
Name: Zaiin, Age: 20, Average Grade: 84.33
Name: Shaik, Age: 22, Average Grade: 80.00

👉 This program uses:
OOP (Class Student) for encapsulation.
Functions (calculate_average, display_details, display_summary).
Loop to handle multiple students.
Do you want me to also add features like grading scale (A, B, C, D, F) along with average marks?
'''


#✅ Full Python Code
# 🎯 Student Grading System using OOP + Functions

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    # Function to calculate average
    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    # Function to display student details
    def display_details(self):
        avg = self.calculate_average()
        print(f"Name: {self.name}, Age: {self.age}, Average Grade: {avg:.2f}")


# Function to display summary of all students
def display_summary(students_list):
    print("\n📌 Student Summary Report:")
    for student in students_list:
        student.display_details()


# ---------------- MAIN PROGRAM ----------------
students = []  # list to store student objects

while True:
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    
    # Accept grades as comma separated values
    grades = list(map(int, input("Enter grades separated by space: ").split()))
    
    # Create Student object
    student = Student(name, age, grades)
    students.append(student)
    
    choice = input("Do you want to add another student? (yes/no): ").lower()
    if choice == "no":
        break

# Display report
display_summary(students)