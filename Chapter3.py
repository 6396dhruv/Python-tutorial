name = "dhruv"
name = 'dhruv'
name = '''dhruv'''

# string slicing
# end index is excluded 0 to 2 and 3 is not included

name1 = name[0:3]
print(name1)

print(name[1])

print(name[-4:-1])

# slicing with skip values
# last value means that we have to skip the 2 values and then print the ans
x = "dhruvpathak"
print(x[1:8:2])  

# functions of strings
# 1- length
print(len(name))
print(name.endswith("ruv"))
print(name.endswith("abs"))
print(name.startswith("dh"))



print(name.capitalize())
print(name.lower())
print(name.find("ru"))
print(name.replace("dhruv", "shivang"))

# escape sequence
a = "dhruv is a good\n boy"
b = "shivang is a good\t boy"
print(a)
print(b)






