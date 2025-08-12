
# n = int(input('Enter a number: '))

# for i in range(1, 11):
#     print(f"{n} X {i} = {n*i}")

# l = ["DHRUV", "SHIVANG", "ABHIHEK", "SHUBHAM"]

# for name in l:
#     if(name.startswith("S")):
#         print(name)

# num = int(input("Enter a number: "))
# for i in range(2, num):
#     if(num%i) == 0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")

# i =1
# sum =0

# while(i<11):
#     sum += i
#     i+=1
#     print(sum)

# n = int(input("Enter the number: "))
# prod = 1
# for item in range(1, n+1):
#     prod = prod*item
# print(f"The factorial of {n} is {prod}")

n = int(input('Enter a number: '))

for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")







