def sumofN(a,t):
 	s=0
 	for i in range(t):
  		s=s+a[i]
 		return s
num=[]
print(end="Enter the value of n:")
n=int(input())
print(end="Enter"+str(n)+"numbers:")
for i in range(n):
	num.insert(i,int(input()))
sum=sumofN(num,n)
print("Sum of"+str(n)+"numbers="+str(sum))
