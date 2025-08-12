# list and tuples
# lists and mutable string are not 
friends = ["dhruv", "shivang", "fruits", 8, False, "july"]
print(friends)
print(friends[0])
friends[0] = "pathak"
print(friends)

print(friends[1:4])

# methods of lists
friends.append("abhishek")
print(friends)
l1 = [2,23,3,4,45,12]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(1, 90)
print(l1)
 
# tuples in python 
# a tuple is a immutable data type in python

a = (1, 2, 3, 4, "dhruv", "shivang", True)
print(type(a))
b =()
# tuple with only one element
c = (1,)
print(type(c))

# tuple methods

no = a.count(3)
print(no)
print(a.index(2))

print(len(a))
# print(min(a))
slice = a[1:3]
print(slice)


