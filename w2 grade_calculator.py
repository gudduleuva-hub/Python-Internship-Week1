def compute_grade(percent):
    if percent >= 90:
        return "A+", "Excellent work!"
    elif percent >= 80:
        return "A", "Very good!"
    elif percent >= 70:
        return "B", "Good!"
    elif percent >= 60:
        return "C", "Need improvement"
    elif percent >= 40:
        return "D", "Below average"
    else:
        return "F", "Fail - Work harder"

def main():
    n = int(input("How many students: "))
    results = []
    for i in range(n):
        name = input(f"Student {i+1} name: ")
        try:
            marks = list(map(float, input("Enter marks separated by space: ").split()))
        except ValueError:
            print("Invalid marks, skipping student.")
            continue
        total = sum(marks)
        percent = (total / (len(marks) * 100)) * 100  # if each subject is out of 100
        grade, comment = compute_grade(percent)
        student = {"name": name, "percent": round(percent,2), "grade": grade, "comment": comment}
        results.append(student)
        print(f"{name}: {student['percent']}% - Grade {grade} - {comment}\n")

    print("All Results:")
    for r in results:
        print(r)

if __name__ == "__main__":
    main()
