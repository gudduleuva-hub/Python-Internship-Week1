# diary_app.py

def write_entry():
    entry = input("Write today's diary entry:\n")
    with open("diary.txt", "a") as f:
        f.write(entry + "\n---\n")
    print("Diary entry saved!")

def read_entries():
    try:
        with open("diary.txt", "r") as f:
            content = f.read()
            print("\n--- Diary Entries ---\n")
            print(content)
    except FileNotFoundError:
        print("No entries found yet.")

print("1. Write entry")
print("2. Read entries")
choice = input("Choose an option: ")

if choice == "1":
    write_entry()
elif choice == "2":
    read_entries()
else:
    print("Invalid choice")
