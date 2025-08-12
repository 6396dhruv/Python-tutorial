#  file input/output

# a file is a data storage device. a python program can talk to the file by reading content from it and 
# writing content to it.

# two types of files
# text Files(txt, .c, etc)
# binary files(.jpg, .dat etc)

# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

# st = "dhruv you are amazing and awesome"
# w = open("file.txt", "w")
# w = open("myfile.txt", "w")
# w.write(st)
# w.close()

# f = open("myfile.txt")

# lines = f.readlines()
# print(lines)
# f.close()

# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()
# f.close()

# s = "dhruv is a good boy"
# f = open("myfile.txt", "a")

# f.write(s)
# f.close()

with open("myfile.txt") as f:
    print(f.read())
















