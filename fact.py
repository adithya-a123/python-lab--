def fact(n):
	if n==1:
	 	return n
	else:
	 	return n*fact(n-1)
number=int(input("Enter a number:"))
result=fact(number)
print("The Factorial of",number,"is",fact(number))
