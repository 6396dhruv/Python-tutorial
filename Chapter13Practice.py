# name = input('Enter name: ')
# marks = int(input("Enter marks: "))
# phone = int(input("Enter phone no: "))

# s = "the name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)

# print(s)

# table = [str(7*i) for i in range(1, 11)]

# a = "\n".join(table)

# print(a)

# def divisble(n):
#     if(n%5 == 0):
#         return True
#     return False

# l = [5, 10, 15, 23, 34, 45, 78]

# div = list(filter(divisble, l))
# print(div)

# from functools import reduce

# def greater(a, b):
#     if(a> b):
#         return a
#     return b

# print(reduce(greater, l))


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()




