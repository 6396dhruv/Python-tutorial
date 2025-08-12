class programmer:

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("dhurv", 100000, 206122)

print(p.name, p.salary, p.pin)


class calculator:

    def __init__(self, n):
        self.n = n
        
    def square(self):
        print(f"the square of number is {self.n*self.n}")
    @staticmethod
    def greet():
        print("hello")

calculate = calculator(5)
calculate.square()
calculate.greet()


from random import randint

class train:
    def __init__(self, trainno):
        self.trainno = trainno

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainno} from {fro} to {to}")

    def getStatus(self, trainno):
        print(f"Train no: {trainno} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainno} from {fro} to {to} is {randint(222, 555)}")


t = train(12399)
t.book("Delhi", "Auraiya")

