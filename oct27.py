'''
def myfun(num):
    print("Hello how are you")
    num = 6
    f = 1
    for i in range(num,0,-1):
        f = f*i
    print("Factorial result is:",f)
myfun(5)
##########################################

class Student:
    def myfun(num):
        f = 1
        for i in range(num,0,-1):
            f = f*i
        print("Factorial result is:",f)
    def SimpleInterest(p,r,t):
        res = (p*r*t)/100
        print("Simple interest is:",res)
    x = int(input("Enter any number"))
    a = int(input("Enter principle:"))
    b = int(input("Enter rate:"))
    c = int(input("Enter time:"))
    myfun(x)
    SimpleInterest(a, b, c)
    
        

'''

#####################################       
        
        
class Student:  # class creation
    name = "Avanish singh"  # class variable 
    print("Class variable inside class",name)
    def myfun(self, num):  # instance method
        f = 1   # local variable
        for i in range(num,0,-1):
            f = f*i
        print("Factorial result is:",f)
    def SimpleInterest(self,p,r,t): # instance method
        res = (p*r*t)/100  # local variable 
        print("Simple interest is:",res)
   
obj = Student()   # object creation
obj.myfun(6)
obj.SimpleInterest(1000,5,4)
print("Class variable outside class using object:",obj.name)
print("Class variable outside class using class:",Student.name)

    
    


