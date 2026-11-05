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

def age_in_months(birthday):
    born = datetime.strptime(birthday, "%m/%d/%Y").date()
    today = date.today()
    months = (today.year - born.year) * 12 + today.month - born.month
    if today.day < born.day:
        months -= 1
    return max(months, 0)

class Baby:
    def __init__(self, name, birthday=None, weightOZ=130, height=20):
        self.name = name
        if birthday is None:
            birthday = date.today().strftime("%m/%d/%Y")
        self.birthday = birthday
        self.weightOZ = weightOZ
        self.height = height
        self.mood = DEFAULT_MOOD
        self.feedings = 0
        self.drinks = 0

    def eat(self, food="vegetables"):
        self.weightOZ += 11
        self.feedings += 1
        if food == "vegetables":
            self.cry()
        elif food == "fruit" or food == "goodies":
            self.laugh()
        elif food == "cereal":
            self.sleep()
        else:
            print("\nBaby: Yum Yum in my Tum Tum!")
            self.mood = "Content"

        if self.feedings % 3 == 0:
            self.poop()
        self.check_burp()

    def check_burp(self):
        if (self.feedings + self.drinks) % 3 == 0:
            self.burp()

    def drink(self):
        self.weightOZ += 8
        self.drinks += 1
        self.mood = "Content"
        print("\nBaby: This has quenched my thirst very well.")
        if self.drinks % 3 == 0:
            self.pee()
        self.check_burp()

    def poop(self):
        print("-Baby poops-")
        self.weightOZ -= 5
        self.mood = "Content"

    def pee(self):
        print("-Baby pees-")
        self.weightOZ -= 4
        self.mood = "Content"

    def laugh(self):
        print("\nHAHAHAHAHAHAHAHAHA")
        self.mood = "Happy"

    def scream(self):
        print("\nAAAAAAAAAAAAAAAAAAAAAAHAAAAAAAAAAH!")
        self.mood = "Mad"

    def cry(self):
        print("\nBaby: WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWAAAAAAAAAAAAAAAAAAA!")
        self.mood = "Sad"

    def sleep(self):
        print("\n-Baby falls asleep dreaming about puppies-")
        self.mood = "Content"

    def burp(self):
        print("-Baby burps-")
        self.mood = "Happy"

    def introduce(self):
        thing = random.choice(FUNNY_THINGS)
        print(f"\nBaby: Hi! My name is {self.name}.")
        years, months = divmod(age_in_months(self.birthday), 12)
        year_text = f"{years} year{'s' if years != 1 else ''}"
        month_text = f"{months} month{'s' if months != 1 else ''}"
        print(f"I am {year_text} and {month_text} old and I weigh {ounces_to_pounds(self.weightOZ)} lbs.")
        print(f"I really like to {thing}!")

    def display_status(self):
        print("\n--- Baby Status ---")
        print(f"Name: {self.name}")
        print(f"Birthday: {self.birthday}")
        print(f"Feedings: {self.feedings}")
        print(f"Drinks: {self.drinks}")
        print(f"Weight: {self.weightOZ} oz")
        print(f"Weight: {ounces_to_pounds(self.weightOZ)} lbs")
        print(f"Height: {self.height} in")
        print(f"Mood: {self.mood}")
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

baby = Baby(name, birthday, weightOZ, height)

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
        foods = {"1": "vegetables", "2": "fruit", "3": "goodies", "4": "cereal"}
        while True:
            print("\n-- Food List --")
            print("1. Vegetables")
            print("2. Fruit")
            print("3. Goodies")
            print("4. Cereal")
            print("5. Exit")
            choice = input("Pick a food (1-5): ").strip()
            if choice in foods:
                baby.eat(foods[choice])
                break
            elif choice == "5":
                break
            print("Please enter a number from 1 to 5.")
    elif userInput == "drink":
        baby.drink()
    elif userInput == "laugh":
        baby.laugh()
    elif userInput == "sleep":
        baby.sleep()
    elif userInput == "cry":
        baby.cry()
    elif userInput == "status":
        baby.display_status()
    elif userInput == "introduce":
        baby.introduce()
    elif userInput == "home":
        babyLoop = False
        baby.display_status()
        baby.introduce()
    else:
        print("WRONG COMMAND IDIOT")
