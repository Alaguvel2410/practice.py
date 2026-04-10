student = {
    "name": "Alaguvel",
    "course": "Python Full Stack",
    "city": "Chennai",
    "cgpa": 7.93,
    "status": "Final Year"
}

print("STUDENT DETAILS")
for key, value in student.items():
    print(key.capitalize(), ":", value)

student["city"] = "Thoothukudi"
student["language"] = "Python"

print("\nUpdated City:", student["city"])
print("New Key:", student["language"])
