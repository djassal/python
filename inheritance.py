class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        
    def printName(self):
        print(self.fname,self.lname)
        
class Student(Person):
    def printStat(self):
        print("Student class.")

x = Person('john','cena')
x.printName()

y = Student('mike','ross')
y.printName()
