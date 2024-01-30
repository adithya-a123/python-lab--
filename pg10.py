n=int(input("Enter a number:"))
def sum(num):
  a=0
  if num<=1:
    print(num)
    
  else:
   for i in range(1,num+1):
     a=a+i
  return a
print("The sum of",n,"number is",sum(n)) 
