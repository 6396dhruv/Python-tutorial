# functions in python - A function is a group of statement performing a specific task.

# function definition

# def avg():
#     n1 = int(input('enter first numner: '))
#     n2 = int(input('enter second number: '))
#     n3 = int(input('enter third number: '))

#     average = (n1+n2+n3)/3
#     print(average)

# # function call
# avg()
# # avg()
# # avg()

# def goodday():
#     print("good day")
# goodday()

# function with arguments

def greet(name, end):
    print("good day "+ name)
    print(end)

greet("dhruv", "thanks")

def hello(name):
    print("hey " + name)
    return hello

a = hello("Dhruv")
print(a)

# default arguments

def good(name, end = "thanks"):
    print(f"Good day, {name}")
    print(end)

good("Dhruv")
good("Shivang", "thank you")

# reccursion function - when a function call itself

def factorial(num):
    if(num == 1):
        return 1
    else:
        return num*factorial(num-1)
    
a = factorial(5)
print(a)




















