def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    with open("students.txt", "a") as file:
        file.write(roll + "," + name + "," + marks + "\n")
    print("Student record added successfully\n")


def view_students():
    print("\n--- Student Records ---")
    with open("students.txt", "r") as file:
        data = file.read()
        if data.strip() == "":
            print("No records found")
        else:
            print(data)


while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Exiting program")
        break
    else:
        print("Invalid choice\n")
