try:
    n = int(input("Enter number for table: "))
    upto = int(input("Upto (e.g., 10): "))
    for i in range(1, upto+1):
        print(f"{n} x {i} = {n*i}")
except ValueError:
    print("Please enter integers.")
