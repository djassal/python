class Base1:
    def __init__(self):
        self.str1 = 'geek1'
        print('Base1')

class Base2:
    def __init__(self):
        self.str2 = 'geek2'
        print('Base2')

class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
        
ob = Derived()