str=str.lower(input("Enter a string:"))
char=str[0]
x=str.replace(char,'$')
x=char+x[1:]
print(x)
