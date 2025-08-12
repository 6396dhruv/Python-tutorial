# f = open("Poem.txt")
# c = f.read()
# if("teinkle" in c):
#     print("twinkle is present in content")
# else:
#     print('not present ')
# f.close()

# import random

# def game():
#     print("You are playing the game...")
#     score = random.randint(1, 60)
#     with open("highscore.txt") as f:
#         highscore = f.read()
#         if(highscore != ""):
#             highscore = int(score)
#         else:
#             highscore =0    

#     print(f"Your score is {score}")
#     if(score > highscore):
#         # write this score to the file
#         with open("highscore.txt", "w") as f:
#             f.write(str(score))
#     return score

# game()

# def generateTable(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} x {i} = {n*i}\n"

#     with open(f"table/table_{n}", "w") as f:
#         f.write(table)


# for i in range(2, 21):
#     generateTable(i)

# word = "Donkey"
# with open("file.txt", "r") as f:
#     content = f.read()
# newcontent = content.replace(word, "######")

# with open("file.txt", "w") as f:
#     content = f.write(newcontent)

# with open("file.txt") as f:
#     content = f.read()

# if("python" in content):
#     print("yes present")
# else:
#     print("not present")


# with open("file.txt") as f:
#     content = f.read()

# with open("highscore.txt", "w") as f:
#     f.write(content)

