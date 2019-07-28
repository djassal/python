class Employee:
     
    def __init__(self,name):
        self.name = name
        print("Emp name is: ", self.name)
                
    def greetEmp(self):
        print("Welcome ",self.name)
        
e1 = Employee('jack')
e1.greetEmp()

