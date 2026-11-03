

MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 50
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

students = []
eligible_students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    app_id = int(input("Application ID: "))
    name = input("Student Name: ")

    subjects = int(input("Number of subjects: "))
    marks = []

    for j in range(subjects):
        mark = float(input(f"Enter marks in subject {j + 1}: "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    aggregate = sum(marks) / len(marks)

    
    if (aggregate >= MIN_AGGREGATE
        and min(marks) >= MIN_SUBJECT_MARK
        and attendance >= MIN_ATTENDANCE
        and income <= MAX_INCOME):

        students.append({
            "id": app_id,
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["id"]
    )
)

scholarships = int(input("\nEnter number of scholarships: "))

print("\n----- SCHOLARSHIP RESULTS -----")

if len(students) == 0:
    print("No eligible students found.")

else:
    for rank, student in enumerate(students, start=1):

        if rank <= scholarships:
            status = "Selected"
        else:
            status = "Not Selected"

        print("\nRank:", rank)
        print("Application ID:", student["id"])
        print("Name:", student["name"])
        print("Aggregate:", round(student["aggregate"], 2), "%")
        print("Attendance:", student["attendance"], "%")
        print("Family Income: Rs.", student["income"])
        print("Status:", status)
