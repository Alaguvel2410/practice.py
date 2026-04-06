# Student Grade Calculator
students = [
    {"name": "Alaguvel", "marks": [85, 90, 78, 92, 88]},
    {"name": "Rahul",    "marks": [70, 65, 80, 75, 60]},
    {"name": "Priya",    "marks": [95, 98, 92, 97, 99]},
]

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"

print("=" * 40)
print("       STUDENT GRADE REPORT")
print("=" * 40)

for student in students:
    avg = sum(student["marks"]) / len(student["marks"])
    grade = calculate_grade(avg)
    print(f"Name    : {student['name']}")
    print(f"Average : {avg:.2f}%")
    print(f"Grade   : {grade}")
    print("-" * 40)
