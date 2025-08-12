# walrus operator in python - (:=)
# walrus - this operator allow you to assign values to the variables as part of an expression.

if(n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long {n} element, expected <=3")

# type definitions in python

from typing import List, Tuple, Union, Dict

n : int = 5

name: str = "dhurv"

def sum(a: int, b: int) -> int:
    return a+b

print(sum(3, 4))

# list of integers

number : list[int]  = [1, 2, 3, 4]

# tuple of string and integers
person : tuple[str, int] = ("Dhruv", 10)

# dictionary with string key and integer value

scores : dict[str, int] = {"dhruv": 10, "shivang": 20}

# union type for holding more than one variable same time

identity : Union[int, str] = "2j2k3k"

# match case in python - similar to switch statement

def server(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Page not found"
        case 500:
            return "unknown status"
        
print(server(404))

# dictionary merge and update

dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd': 4}

merged = dict1|dict2
print(merged)

# with(
#     open("file.txt") as f1,
#     open("myfile.txt") as f2
# ):    
    
# exception handling in python
# try:

#     a = int(input('enter a number: '))
#     print(a)
# except Exception  as e:

#     print(e)

a = int(input("Enter first number: "))
b = int(input("Enter second numner: "))

if(b == 0):
    raise ZeroDivisionError("This cant be divided with zero sorry...")
else:
    print(f"The division is {a/b}")

# when to use else and finally with try statement

# try with else:-

# try:
#     a = int(input('enter a number: '))
#     print(a)
# except Exception  as e:
#     print(e)

# else:
#     print("I am inside else")

# try with finally

try:
    a = int(input('enter a number: '))
    print(a)
except Exception  as e:
    print(e)

finally:
    print("i am inside finally")


# if name == main in python

def myfunc():
    print("hello world")

myfunc()

print(__name__)

# enumerate function in python

l = [1,2,3,4,5,6]
# index =0
# for item in l:
#     print(f"the item number at index {index} is {item}")
#     index +=1

# the above list can be simplified using enumerate function

for index,item in enumerate(l):
    print(f"the item number at index {index} is {item}")

# list comprehensions in python

mylist = [2,3,4,5,6]

sqaurelist = [i*i for i in mylist]

print(sqaurelist)


    












 






