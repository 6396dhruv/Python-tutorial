# fake headline generator

# step 1 - import the random module
import random

# create subjects
subjects = ["salman khan", "virat kohli", "rohit sharma", "A group of monkey", "prime minister modi", "auto rikshaw driver", "jaat"]

actions = ["launches", "cancels", "eats", "dances with", "declares war on", "orders", "celebrates"]

places_of_actions = ["at red fort", "plate of samosa", "inside parliamememt", "during ipl match", "at india gate", "at ganga ghat",
"local train"]


# start the headline generation loop
# strip() - l strip and r strip for left and right space

while True:
    subject =  random.choice(subjects)
    action = random.choice(actions)
    places = random.choice(places_of_actions)


    headline = f"Breaking News: {subject} {action} {places}"

    print("\n" + headline)
    user = input("\n Do you want another headline? (yes/no).").strip().lower()
    if user == "no":
        break

# print a goodbye message
print("\n Thanks for using the fake news headline generator have fun!")
