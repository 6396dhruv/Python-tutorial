# oops in python
# class and object

# class- 
class employee:
    # name = "Dhruv"
    language = "py"
    salary = 100000

dhruv = employee()
dhruv.name = "Dhruv"
print(dhruv.name,dhruv.language, dhruv.salary)

shivang = employee()
shivang.name = "shivang" #instance attribute
print(shivang.name,shivang.language, shivang.salary)

# here name is object attribute and salary and language are class attribute as they directly belong to the class.

# noun - class -> employee
# adjectives - Attributes ->name, age, salary
# verbs - Methods -> getSalary(), increment()

# class attributes - 

# instance vs class attribute
# instance attribute will take prefrence over the class attribute it will print c++

dhruv.language = "c++"
print(dhruv.language)

# self parameter -

class student:
    stream = "science"
    seats = 50

    def __init__(self, name, stream, seats):  # this is called as dunder methods - init it is automatically called
        self.name = name
        self.stream = stream
        self.seats = seats
        print("i am creating an object")

    def getInfo(self):
        print(f"the stream is {self.stream}, seats are {self.seats}")
    @staticmethod  # ye ab self nhi lega oibject ya property nhi chahieye
    def greet():
        print("hello everyone")

abhi = student("dhruv", "commerce", 10)
abhi.getInfo()
abhi.greet()
# student.getInfo(abhi)

# __init__() constructer

# it takes self argument nad can also tale further arguments











