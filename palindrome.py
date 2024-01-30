def is_palindrome(n):
	n_str=str(n)
	n_rev=n_str[::-1]
	if n_str==n_rev:
  		return True
  	return False
n=str(input("Enter a input:"))
result=is_palindrome(n)
if(result==True):
  	print("The input is palindrome")
else:
  	print("The input is not palindrome")

