print() # blank line
print("Enter your points for " + course)

a = int(input("Points -> "))

for course in my_courses

    redo = input("Do you need to re-do these grades? (y/n)")
if (redo == "y"):
	check_grades = True
else:
	check_grades = False

if (a >= 90):
	print("A")
elif (a >= 80):
	print("B")
elif (a >= 70):
	print("C")
elif (a >= 60):
	print("D")
else:
	print("F")