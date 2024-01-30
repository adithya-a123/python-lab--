num_students=int(input("Enter the number of students:"))
days=int(input("Enter the number of working days:"))
student_list = []

for i in range(num_students):
	name=input(f"Enter the name of student:")
	attendance=int(input("no:of days present:"))
	attendance_percentage = ((attendance / days) * 100)
	student_list.append((name,attendance_percentage))
	student_list.sort(reverse=True)
print("Student List:")
for student in student_list:
	print(f"{student[0]}-{student[1]}%")
