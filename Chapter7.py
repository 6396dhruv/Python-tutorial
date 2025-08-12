# loops in python

i = 0
while(i<6):
    print(i)
    i +=1

l = [1, "dhruv", False, "this", "shivang", "abhishek"]

j=0
while(j< len(l)):
    print(l[j])
    j+=1

for item in l:
    print(item)

for i in range(1,10,2):
    print(i)

t = (2, 3, 4, 4)
for item in t:
    print(item)

s = "dhruv"
for i in s:
    print(i)

# for loop with else

list = [10,9,8,7]
for item in list:
    print(item)
else:
    print("this is ended")

for i in range(10,20):
    if(i == 15):
        break
    print(i)

for i in range(10,20):
    if(i == 15):
        continue
    print(i)

for i in range(500):
    pass

i=0
while(i<5):
    print(i)
    i+=1







