# to activate the virtual environment env -- we write -- .\env\Scripts\activate.ps1

# to deactivate the environment -- we use -- deactivate

# pip install virtualenv
# virtualenv env

# pip freeze - give all the packages 
# pip freeze > requirement.txt
# pip install -r .\requirement.txt - install all the packages which is present in requirement.txt

# LAMBDA FUNCTION 

square = lambda x: x*x

print(square(5))

sum = lambda a,b,c: a+b+c

print(sum(1,2,3))

# join method in python

a = ["dhruv", "abhishek", "ujjwal"]

final = "-".join(a)
print(final)

# Map, Filter, Reduce method in python
# map will tale function and input list map(function, inputlist)
l = [1,2,3,4,5]

square = lambda x: x*x

sqlist = map(square, l)
print(list(sqlist))

def even(n):
    if(n%2 == 0):
        return True
    return False

onlyeven = filter(even, l)
print(list(onlyeven))

from functools import reduce
def sum(a, b):
    return a+b
mul = lambda x,y:x*y
print(reduce(sum,l))








