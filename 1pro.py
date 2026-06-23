"""1️⃣ Student Management System (Very Important)
Isme:

✔ Add student
✔ Delete student
✔ Update student
✔ Search student
✔ Save data in file

Concepts used:
OOP
File Handling
Dictionary
Functions

Example Features:
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit

👉 Ye first must project hai."""

# student = {}

# while True:
#     print("\n=======================student management system==============================")
#     print("1. Add Student")
#     print("2. View Student")
#     print("3. Search student")
#     print("4. delete Student")
#     print("5. save data")
#     print("6. update data")
#     print("7. Exit")

#     choice = input("please chooce an point: ")

#     if choice == "1":
#         print("1. Add Student")

#     elif choice == "2":
#         print("2. View Student")

#     elif choice == "3":
#         print("3.search student")

#     elif choice == "4":
#         print("4. delete student")

#     elif choice == "5":
#         print("5.save data")

#     elif choice == "6":
#         print("6. update data")
    
#     elif choice == "7":
#         print("7. Exit")

#     else:
#         print("Error")

#     if choice == "1":
#         name = input("Add Student: ")
#         student_id = int(input("enter a id: "))
#         age = int(input("enter a age: "))
#         marks = int(input("enter a marks: "))

#         student[student_id] = {
#         "name": name,
#         "age": age,
#         "marks": marks
#         }

#     if choice == "2":
#         if not student:
#             print("not student found!")
#         else:
#             print("\nstudent records: ")
#             for student_id, details in student.items():
#                 print(f"ID: {student_id}")
#                 print(f"Name: {details['name']}")
#                 print(f"Age: {details['age']}")
#                 print(f"Marks: {details['marks']}")
#                 print("-" * 20)

#     if choice == "3":
#         student_id = int(input("Enter Student ID to search: "))

#         if student_id in student:
#             details = student[student_id]
#             print("\nStudent Found:")
#             print(f"ID: {student_id}")
#             print(f"Name: {details['name']}")
#             print(f"Age: {details['age']}")
#             print(f"Marks: {details['marks']}")
#         else:
#             print("Student not found!")

#     if choice == "4":
#         student_id = int(input("Enter Student ID to delete: "))

#         if student_id in student:
#             del student[student_id]
#             print("Student deleted successfully!")
#         else:
#             print("Student not found!")

#     if choice == "6":
#         student_id = int(input("enter a student id for update"))
#         if student_id in student:
#             print("current details:")
#             print(f"Name: {student[student_id]['name']}")
#             print(f"Age: {student[student_id]['age']}")
#             print(f"Marks: {student[student_id]['marks']}")

#             name = input("Enter New Name: ")
#             age = int(input("Enter New Age: "))
#             marks = int(input("Enter New Marks: "))

#             student[student_id] = {
#                 "name": name,
#                 "age": age,
#                "marks": marks
#              }

#             print("Student Updated Successfully!")
#         else:
#              print("Student not found!")

#     if choice == "7":
#         print("you'r out of programe")
#         break

#     if choice == "5":
#         import json

#         with open ("students.json", "w")as file:
#             json.dump(student, file, indent=4)
#         print("Data Saved Successfully!")


import json
import os


class StudentManagement:

    def __init__(self):
        self.file = "students.json"
        self.students = self.load_data()


    # Load data from file
    def load_data(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                return json.load(f)
        return {}


    # Save data to file
    def save_data(self):
        with open(self.file, "w") as f:
            json.dump(self.students, f, indent=4)


    # Add student
    def add_student(self):
        roll = input("Enter Roll Number: ")

        if roll in self.students:
            print("Student already exists!")
            return

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        self.students[roll] = {
            "name": name,
            "age": age,
            "course": course
        }

        self.save_data()

        print("Student added successfully!")


    # Delete student
    def delete_student(self):
        roll = input("Enter Roll Number to delete: ")

        if roll in self.students:
            del self.students[roll]
            self.save_data()
            print("Student deleted successfully!")
        else:
            print("Student not found!")


    # Update student
    def update_student(self):
        roll = input("Enter Roll Number to update: ")

        if roll in self.students:

            print("Current Data:")
            print(self.students[roll])

            name = input("Enter New Name: ")
            age = input("Enter New Age: ")
            course = input("Enter New Course: ")

            self.students[roll] = {
                "name": name,
                "age": age,
                "course": course
            }

            self.save_data()

            print("Student updated successfully!")

        else:
            print("Student not found!")


    # Search student
    def search_student(self):
        roll = input("Enter Roll Number to search: ")

        if roll in self.students:
            print("\nStudent Found:")
            print(self.students[roll])

        else:
            print("Student not found!")


    # Display all students
    def show_students(self):
        if len(self.students) == 0:
            print("No students available")

        else:
            print("\nAll Students:")

            for roll, data in self.students.items():
                print(
                    f"Roll: {roll}, "
                    f"Name: {data['name']}, "
                    f"Age: {data['age']}, "
                    f"Course: {data['course']}"
                )



# Main Program

system = StudentManagement()


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Show All Students")
    print("6. Exit")


    choice = input("Enter choice: ")


    if choice == "1":
        system.add_student()


    elif choice == "2":
        system.delete_student()


    elif choice == "3":
        system.update_student()


    elif choice == "4":
        system.search_student()


    elif choice == "5":
        system.show_students()


    elif choice == "6":
        print("Program Closed")
        break


    else:
        print("Invalid Choice!")




    



        

