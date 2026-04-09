# List Operations
languages = ["Python", "SQL", "HTML", "CSS"]

print("All Languages  : " + str(languages))
print("First          : " + languages[0])
print("Last           : " + languages[-1])
print("Total          : " + str(len(languages)))

languages.append("JavaScript")
print("After Append   : " + str(languages))

languages.remove("CSS")
print("After Remove   : " + str(languages))

languages.sort()
print("After Sort     : " + str(languages))

print("Index of SQL   : " + str(languages.index("SQL")))
