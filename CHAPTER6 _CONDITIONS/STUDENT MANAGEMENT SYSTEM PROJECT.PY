'''PROJECT: STUDENT MANAGEMENT SYSTEM PROJECT
USECASE: CREATE A SIMPLE STUDENT MANAGEMENT SYSTEM
OBJECTIVE: BUILD A PYTHON PROGRAM TO MANAGE STUDENT DATA USING VARIOUS DATA STRUCTURES. 
THE PROGRAM SHOULD ALLOW USERS TO:
1. ADD STUDENT INFORMATION (NAME, AGE, GRADES).
2. RETRIEVE INFORMATION ABOUT SPECIFIC STUDENT.
3. DISPLAY A LIST OF ALL STUDENTS.
4. PERFORM OPERATIONS LIKE CALCULATING THE AVERAGE GRADE. 
'''

# Initializing data structure (list of dictionaries)
students = []

# Adding students
student1 = {"name": "alice", "age": 21, "grades": [85, 90, 88]}
student2 = {"name": "bob", "age": 22, "grades": [72, 82, 80]}
students.append(student1)
students.append(student2)

# DISPLAY ALL STUDENTS
print("📋 List of students:")
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']}")


# RETRIEVE A SPECIFIC STUDENT'S INFORMATION
name_to_find = "alice"
for student in students:
    if student["name"] == name_to_find:
        print(f"\n📘 Information for {name_to_find}:")
        print(f"Age: {student['age']}")
        print(f"Grades: {student['grades']}")

# CALCULATE THE AVERAGE GRADE OF A STUDENT
grades = student1["grades"]   # using student1 for example
average_grade = sum(grades) / len(grades)
print(f"\n📊 Average grade for {student1['name']}: {average_grade:.2f}")
