# inheritance and oops concept

class employee:
    company = "TCS"
    name = "dhruv"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.company}")

class coder:
    language = "python"
    def printlanguage(self):
        print(f"Out of all the language here is your language: {self.language}")

class programmer(employee, coder):
    company = "HCL TECH"
    def showlanguage(self):
        print(f"The name is {self.company} and he is good in {self.name} language")
a = employee()
b = programmer()

b.show()
b.showlanguage()
b.printlanguage()