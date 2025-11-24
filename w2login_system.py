# Simple login with hard-coded user for practice
USERNAME = "prathma"
PASSWORD = "intern123"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    u = input("Username: ")
    p = input("Password: ")
    if u == USERNAME and p == PASSWORD:
        print("Login successful! Welcome,", USERNAME)
        break
    else:
        attempts += 1
        print("Incorrect. Attempts left:", max_attempts - attempts)
else:
    print("Too many attempts. Try later.")
