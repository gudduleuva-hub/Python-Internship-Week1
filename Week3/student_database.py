# Student Database using Dictionary

students = {}

def add_student(name, marks):
    students[name] = marks
    print("Student added successfully!")

def search_student(name):
    if name in students:
        print(f"{name} → {students[name]}")
    else:
        print("Student not found.")

def display_all():
    print("\n--- Student List ---")
    for name, marks in students.items():
        print(f"{name}: {marks}")

# Example use:
add_student("Prathma", 92)
add_student("Riya", 89)
search_student("Prathma")
display_all()
