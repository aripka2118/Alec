import random
from datetime import datetime, date

OUNCES_PER_POUND = 16
DEFAULT_MOOD = "content"
FUNNY_THINGS = [
    "chew on the TV remote",
    "stare at the ceiling fan like it owes me money",
    "blow spit bubbles at strangers",
    "throw my food on the floor and watch it fall",
    "hide my face and then yell 'peekaboo!'",
    "babble dramatically at the dog",
    "grab everyone's nose",
]

def ounces_to_pounds(oz):
    return round(oz/OUNCES_PER_POUND, 2)

def eat(weightOZ, feedings):
    weightOZ += 11
    feedings += 1
    
    print("\nBaby: Yum Yum in my Tum Tum!")
    if feedings % 3 == 0:
        weightOZ = poop(weightOZ)

    return weightOZ, feedings, "Happy"

def drink(weightOZ, drinks):
    weightOZ += 8
    drinks += 1
    print("\nBaby: This has quenched my thirst very well.")
    if drinks % 3 == 0:
        weightOZ = pee(weightOZ)

    return weightOZ, drinks, "Content"
    
def poop(weightOZ):
    print("-Baby poops-")
    weightOZ -= 5
    return weightOZ

def pee(weightOZ):
    print("-Baby pees-")
    weightOZ -= 3
    return weightOZ

def laugh():
    print("\nHAHAHAHAHAHAHAHAHA")
    return "Happy"

def cry():
    print("\nBaby: WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWAAAAAAAAAAAAAAAAAAA!")
    return "Sad"

def sleep():
    print("\n-Baby falls asleep dreaming about puppies-")
    return "Content"
def age_in_months(birthday):
    born = datetime.strptime(birthday, "%m/%d/%Y").date()
    today = date.today()
    months = (today.year - born.year) * 12 + today.month - born.month
    if today.day < born.day:
        months -= 1
    return max(months, 0)

def introduce(name, birthday, weightOZ):
    thing = random.choice(FUNNY_THINGS)
    print(f"\nBaby: Hi! My name is {name}.")
    years, months = divmod(age_in_months(birthday), 12)
    year_text = f"{years} year{'s' if years != 1 else ''}"
    month_text = f"{months} month{'s' if months != 1 else ''}"
    print(f"I am {year_text} and {month_text} old and I weigh {ounces_to_pounds(weightOZ)} lbs.")
    print(f"I really like to {thing}!")

def display_status(name, birthday, weightOZ, mood, feedings, drinks, height):
    print("\n--- Baby Status ---")
    print(f"Name: {name}")
    print(f"Birthday: {birthday}")
    print(f"Feedings: {feedings}")
    print(f"Drinks: {drinks}")
    print(f"Weight: {weightOZ} oz")
    print(f"Weight: {ounces_to_pounds(weightOZ)} lbs")
    print(f"Height: {height} in")
    print(f"Mood: {mood}")
    print("-------------------")

print("What is the baby's name?")
name = input("Name: ")

print("\nWhat is your baby's birthday? (MM/DD/YYYY)")
while True:
    birthday = input("Birthday: ")
    try:
        age_in_months(birthday)
        break
    except ValueError:
        print("Please use the format MM/DD/YYYY.")

print("\nWhat is your babies weight in ounces?")
weightOZ = int(input("Weight: "))

print("\nWhat is your babies height in inches?")
height = float(input("Height: "))

babyLoop = True
feedings = 0
drinks = 0
mood = DEFAULT_MOOD

while(babyLoop):
    userInput = ""

    print("\n-- Action List --")
    print("eat")
    print("drink")
    print("laugh")
    print("sleep")
    print("cry")
    print("status")
    print("introduce")
    print("home")

    userInput = input("Please type a command: ").lower()

    if userInput == "eat":
        weightOZ, feedings, mood = eat(weightOZ, feedings)
    elif userInput == "drink":
        weightOZ, drinks, mood = drink(weightOZ, drinks)
    elif userInput == "laugh":
        mood = laugh()
    elif userInput == "sleep":
        mood = sleep()
    elif userInput == "cry":
        mood = cry()
    elif userInput == "status":
        display_status(name, birthday, weightOZ, mood, feedings, drinks, height)
    elif userInput == "introduce":
        introduce(name, birthday, weightOZ)
    elif userInput == "home":
        babyLoop = False
        display_status(name, birthday, weightOZ, mood, feedings, drinks, height)
        introduce(name, birthday, weightOZ)
    else:
        print("WRONG COMMAND IDIOT")

    if (drinks % 3 == 0 and feedings % 3 == 0) and (userInput == "eat" or userInput == "drink"):
        print("-Baby burps-")
        