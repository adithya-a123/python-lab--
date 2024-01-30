n=int(input("enter number of names"))
names=[]
for i in range(n):
      name=input("enter names:")
      names.append(name)
names.sort()
for name in names:
       print(name)
