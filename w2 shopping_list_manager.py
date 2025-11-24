def show_menu():
    print("\n1. Show list\n2. Add item\n3. Remove item\n4. Exit")

shopping = []

while True:
    show_menu()
    choice = input("Choose option: ")
    if choice == "1":
        if shopping:
            print("Shopping list:")
            for i, item in enumerate(shopping, 1):
                print(i, item)
        else:
            print("List is empty.")
    elif choice == "2":
        it = input("Enter item to add: ").strip()
        if it:
            shopping.append(it)
            print(it, "added.")
    elif choice == "3":
        idx = input("Enter item number to remove: ")
        try:
            idx = int(idx)
            removed = shopping.pop(idx-1)
            print(removed, "removed.")
        except (ValueError, IndexError):
            print("Invalid number.")
    elif choice == "4":
        print("Goodbye.")
        break
    else:
        print("Invalid choice.")
