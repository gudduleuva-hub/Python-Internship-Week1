# save_user_data.py

def save_user_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    try:
        with open("userdata.txt", "a") as file:
            file.write(f"{name} - {age}\n")
        print("Data saved successfully!")
    except Exception as e:
        print("Error while saving:", e)

save_user_data()
