def add_student(students):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    score = float(input("Enter student score: "))
    students[name] = {"age": age, "score": score}
    print(f"{name} added successfully!")

def view_all_students(students):
    if not students:
        print("No students found.")
        return
    for name, info in students.items():
        print(f"Name: {name}, Age: {info['age']}, Score: {info['score']}")

def search_student(students):
    name = input("Enter student name to search: ")
    if name in students:
        print(f"Name: {name}, Age: {students[name]['age']}, Score: {students[name]['score']}")
    else:
        print(f"{name} not found.")

def delete_student(students):
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print(f"{name} deleted successfully!")
    else:
        print(f"{name} not found.")

def main():
    students = {}
    while True:
        print("\nStudent Record Manager")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()