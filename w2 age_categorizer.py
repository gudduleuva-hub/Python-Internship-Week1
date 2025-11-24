def categorize_age(age):
    if age < 0:
        return "Invalid age"
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

try:
    a = int(input("Enter age: "))
    print("Category:", categorize_age(a))
except ValueError:
    print("Please enter a number.")
