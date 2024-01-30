def calculator(num1,operator,num2):
	if operator=="+":
		return add(num1,num2)
	elif operator=="-":
		return subtraction(num1,num2)
	elif operator=="/":
		return divide(num1,num2)
	elif operator=="*":
		return multiplication(num1,num2)
	elif operator=="**":
		return power(num1,num2)
	else:
		print("Wrong operator")
def add(num1,num2):
	return num1+num2
def subtraction(num1,num2):
	return num1-num2
def divide(num1,num2):
	return num1/num2
def multiplication(num1,num2):
	return num1*num2
def power(num1,num2):
	return num1**num2
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
operator=input("Enter operation to be performed:+,-,/,*,**:")
print(calculator(num1,operator,num2))
