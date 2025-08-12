# disctionary
# it is mutable
# it is unordered
# it is indexed
# cannot contain dublicate keys

marks = {
    "dhurv": 100,
    "shivang": 50,
    "abhishek": 45,
    "list": [1,2,3]
}

print(marks, type(marks))
print(marks["dhurv"])

# disctionary methods

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"ujjwal": 23, "yuvi": 32})
print(marks)
# below first one returns none and second one prints a error if it is not present in the disctionary
print(marks.get("dhruv")) 
# print(marks["abhi"])

print(marks.clear())

# sets in python
# set are unordered
# set are unindexed
# no way to change items in sets
# cannot contain dublicate values
s = {1,2,3,4,5}
e = set()
# empty set is created using e = set() if you write s = {} this will create a empty disctionary
print(type(e))
print(s)

# set methods
s.add(6)
print(s)
s.pop()
print(s)
print(len(s))
t = {3,4,5,6}
print(s.union(t))
print(s.intersection(t))
print(s-t)
print(s.issubset(t))
print({2}.issubset(s))

















