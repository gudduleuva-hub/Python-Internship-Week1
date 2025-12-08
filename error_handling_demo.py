# error_handling_demo.py

filename = input("Enter filename: ")

try:
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File not found!")
except PermissionError:
    print("Error: You don't have permission to open this file.")
except Exception as e:
    print("Unexpected error:", e)
