# String Operations 
name = "Alaguvel"
course = "Python Full Stack"
city = "Chennai"

print("Name         : " + name)
print("Course       : " + course)
print("City         : " + city)
print("Name Length  : " + str(len(name)))
print("Uppercase    : " + name.upper())
print("Lowercase    : " + name.lower())
print("Reversed     : " + name[::-1])
print("Replace      : " + course.replace("Python", "Django"))
print("Starts with A: " + str(name.startswith("A")))
print("Contains Full: " + str("Full" in course))
