l = [1,2,3,4,5,6,7]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i==6:
        print(item)

n = int(input('enter a number: '))

table = [n*i for i in range(1, 11)]

print(table)



