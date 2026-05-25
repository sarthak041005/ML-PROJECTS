# class Employee:
    
#     language="Python"
#     salary=120000

# sarthak= Employee()
# sarthak.name="sarthak"
# print(sarthak.name, sarthak.salary, sarthak.language)
# harry=Employee()
# harry.name="harry gellar"
# print(harry.name, harry.salary, harry.language)
# class Employee:
#     language="Python"
#     salary="120000"
# sarthak=Employee()
# sarthak.name="Sarthak"
# print(sarthak.language, sarthak.name)

# harry=Employee()
# harry.name="Harry"
# print(harry.salary, harry.name)
# class Employee:
#     name="sarthak"
#     language="py"
#     salary=120000
#     def __init__(self,name, language, salary):
#         print(self.name, self.language)
#         name="harry"

# sarthak=Employee("ross", "java", 130000)
# print(sarthak.salary)
# class for storing programmer's info
# class Programmer:
#     company= "microsoft"
#     def __init__(self, name, salary):
#         self.name=name
#         self.salary=salary
# prog= Programmer("sarthak", "120000")
# print(prog.salary, prog.name)
# prog2=Programmer("harry", "130000")
# print(prog2.name, prog2.salary)
# Calculator
# class Calculator:
#         def __init__(self,num):
#             self.num=num
#         def sqr(self,num):
#             print(f"the square is {num*num}")
#         def cube(self,num):
#             print(f"the cube is {num*num*num}")
#         def sqrt(self, num):
#              print(f"the sqrt is {num**(1/2)}")
# a=Calculator(3)
# a.sqr(4)
# a.cube(3)
# a.sqrt(64)
# inheritance
# class Employee:
#     company="ITC"
#     def show(self):
#         print(f"{self.name}{self.company}")
# class Programmer(Employee):
#     company="ITC INFOTECH"
#     def showLanguage(self):
#         print(f"{self.language}")
# a = Employee()
# b= Programmer()
# print(a.company, b.company)
# class Employee:
#     company= "ITC"
#     def show(self):
#         print(f"{self.company}")

# class Coder:
#     language="Python"
#     def showLang(self):
#         print(f"{self.language}")

# class Programmer(Employee, Coder):
#     city="Blr"
#     def show(self):
#         print(f"{self.city}")
# a=Employee()
# b=Coder()
# c=Programmer()
# a.show()
# b.showLang()
# c.show()

# class Employee:
#     city= "blr"
#     def showcity(self):
#         print(f"{self.city}")
# class Coder:
#     language="python"
#     def showLang(self):
#         print(f"{self.language}")
# class Programmer(Employee, Coder):
#     salary=120000
#     def showSalary(self):
#         print(f"{self.salary}")
# a=Employee()
# a.showcity()
# b=Coder()
# b.showLang()
# c=Programmer()
# c.showSalary()
# # print(a.city, b.language, c.salary)
# multilevel inheritance
# class Employee:
#     company="Google"
#     def __init__(self):
#          print("constructor of employee")
#     def getCompanyName(self):
#         print(self.company)
# class Programmer(Employee):
#     Language="Python"
#     def __init__(self):
#          print("constructor of programmer")
#     def getLang(self):
#         print(self.Language)
# class Manager(Programmer):
#     Salary="100000"
    
#     def __init__(self):
#         super().__init__()
#         print("constructor of manager")
#         print(self.Salary)
# # a = Employee()
# # a.getCompanyName()
# # b=Programmer()
# # b.getCompanyName()  
# c=Manager()
# c.getSalary()
# c.getLang()
# class method
# class Employee:
#     a=1
#     @classmethod
#     def show(cls):
#         print(f"value of a is {cls.a}")
# b=Employee()
# b.a=45
# b.show()