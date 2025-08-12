
# a1 = int(input("Enter number 1: "))
# a2 = int(input("Enter number 2: "))
# a3 = int(input("Enter number 3: "))

# if(a1>a2 and a1>a3):
#     print("Greater number is: ", a1)
# elif(a2>a1 and a2>a3):
#     print("Greater number is: ", a2)
# else:
#     print("Greater number is: ", a3)

# marks1 = int(input("Enter marks 1: "))
# marks2 = int(input("Enter marks 2: "))
# marks3 = int(input("Enter marks 3: "))

# totalPercent = ((marks1+marks2+marks3)/300)*100

# if(totalPercent>=40):
#     print("You are passed")
# else:
#     print("You are failed")

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"

message = input("Enter your comment: ")

if(p1 in message or p2 in message or p3 in message):
    print("this comment is a spam")
else:
    print("this is not a scam you can proceed")

marks = int(input("Enter your marks: "))

if(marks<100 and marks >=90):
    grade = "EX"
elif(marks<90 and marks >=80):
    grade = "A"
elif(marks<80 and marks >=70):
    grade = "B"
elif(marks<70 and marks >=60):
    grade = "C"
elif(marks<60 and marks >=50):
    grade = "D"
elif(marks<50 and marks >=0):
    grade = "F"

print("Your grade is: ", grade)


