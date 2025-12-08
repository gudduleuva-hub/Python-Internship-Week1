# -----------------------------------------
# Final Project - Contact Management System
# Week 4 - Internship Project
# -----------------------------------------

CONTACT_FILE = "contacts.txt"

# Function to add contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    # Saving into file
    try:
        with open(CONTACT_FILE, "a") as file:
            file.write(f"{name},{phone}\n")
        print("Contact added successfully!\n")
    except:
        print("Error while saving the contact.\n")


# Function to search contact by name
def search_contact():
    search_name = input("Enter name to search: ")

    try:
        with open(CONTACT_FILE, "r") as file:
            found = False
            for line in file:
                name, phone = line.strip().split(",")
                if name.lower() == search_name.lower():
                    print(f"Contact Found → Name: {name}, Phone: {phone}\n")
                    found = True
                    break
            if not found:
                print("Contact not found.\n")
    except FileNotFoundError:
        print("No contacts saved yet.\n")


# Function to display all contacts
def display_contacts():
    try:
        with open(CONTACT_FILE, "r") as file:
            print("\n--- All Contacts ---")
            for line in file:
                name, phone = line.strip().split(",")
                print(f"Name: {name} | Phone: {phone}")
            print()
    except FileNotFoundError:
        print("No contacts available.\n")


# Main menu
def main():
    while True:
        print("=== Contact Management System ===")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            display_contacts()
        elif choice == "4":
            print("Thank you for using the Contact Manager!")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run the main program
main()
