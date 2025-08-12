
def greater(a, b, c):
    if(a>b and a>c):
        print(f"Greater is {a}")
    elif(b>a and b>c):
        print(f"Grester is {b}")
    else:
        print(f"Greater is {c}")

a = 2
b= 3
c=4
print(greater(a, b, c))

def sum(num):
    if(num == 1):
        return 1
    return sum(num-1)+ num

print(f"The sum of n natural number are: {sum(5)}")


    
