name = input("enter your name: ")

print(f'Good Afternoon {name}')
print("good afternoon " + name)
# second question

letter = '''Dear <|Name|>, You are selected! <|Date|> '''

print(letter.replace("<|Name|>", "Dhruv").replace("<|Date|>", "05/08/2025"))

# third - detect double space in a string

name = "dhruv is a excellent  boy and have knowledge too"
print(name.find("  "))

# Strings are immutable you can not change them by running function and updating it


