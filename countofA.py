x=input("Enter first name:")
list=x.split(" ")
count=0
for i in list:
	for j in i:
		if 'a'==j or 'A'==j:
			count=count+1
print("occurrence of 'a' in the list:",count)
