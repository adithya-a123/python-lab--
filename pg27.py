dic={}
n=int(input("Total number of elements in dictionary:"))
for i in range(n):
    name=input("Enter name:")
    dic[name]=None
    
l=list(dic.items())
l.sort()
print(l)
l.sort(reverse=True)
print(l)

    
