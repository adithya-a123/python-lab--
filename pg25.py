student={}
n=int(input("Enter the number of student:"))
for i in range(n):
	name=input("Name:")
	age=int(input("Age:"))
	grade=input("Grade:")
	student[name]=age,grade
	print(student)
