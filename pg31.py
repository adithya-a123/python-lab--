class rect:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    
    def area(self):
        return self.breadth*self.length
    
    def per(self):
        return 2*(self.length+self.breadth)
    
a=int(input("Enter length of rectangle:"))
b=int(input("Enter breadth of rectangle:"))
obj=rect(a,b)#Creating an object 'obj' of class rect

print("Area of rectangle:",obj.area())
print("Perimeter of rectangle:",obj.per())
