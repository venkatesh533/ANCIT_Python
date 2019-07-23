
'''
Demo on inheritance
'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printfun(self):
        print(self.name,self.age)

class Employee(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        super().printfun()
        #Person.__init__(self,name,age)
        #Person.printfun(self)

obj = Employee('abc',33)
#print(obj.name,obj.age)
