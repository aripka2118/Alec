import random
import time
from datetime import datetime, date

ACTION_DELAY_SECONDS = 1

OUNCES_PER_POUND = 16
DEFAULT_HEIGHT = 20
DEFAULT_WEIGHT = 130
FOOD_WEIGHT_GAIN = 11
DEFAULT_FOOD = "veggies"
FOOD_LIST = ["veggies", "fruit", "goodies", "cereal"]
DRINK_WEIGHT_GAIN = 8
DEFAULT_DRINK = "water"
DRINK_LIST = ["milk", "water", "soda", "juice"]
MOOD_CONTENT = "Content"
MOOD_HAPPY = "Happy"
MOOD_MAD = "Mad"
MOOD_SAD = "Sad"
DEFAULT_MOOD = MOOD_CONTENT
FUNNY_THINGS = [
    "chew on the TV remote",
    "stare at the ceiling fan like it owes me money",
    "blow spit bubbles at strangers",
    "throw my food on the floor and watch it fall",
    "hide my face and then yell 'peekaboo!'",
    "babble dramatically at the dog",
    "grab everyone's nose",
]

class Baby:
    def __init__(self, name, birthday=None, weight=DEFAULT_WEIGHT, height=DEFAULT_HEIGHT):
        self.name = name
        if birthday is None:
            birthday = date.today().strftime("%m/%d/%Y")
        self.birthday = birthday
        self.weight = weight
        self.starting_weight = weight
        self.height = height
        self.mood = DEFAULT_MOOD
        self.feedings = 0
        self.drinks = 0

    def eat(self, food=DEFAULT_FOOD):
        self.weight += FOOD_WEIGHT_GAIN
        self.feedings += 1
        print(f"\nBaby ate {food} and has gained {ounces_to_pounds(FOOD_WEIGHT_GAIN)} lbs")
        if food == DEFAULT_FOOD:
            self.cry()
        elif food == "fruit" or food == "goodies":
            self.laugh()
        elif food == "cereal":
            self.sleep()
        else:
            print("\nBaby: Yum Yum in my Tum Tum!")
            self.mood = MOOD_CONTENT

        if self.feedings % 3 == 0:
            self.poop()
        self.check_burp()

    def check_burp(self):
        if (self.feedings + self.drinks) % 3 == 0:
            self.burp()

    def drink(self, beverage=DEFAULT_DRINK):
        self.weight += DRINK_WEIGHT_GAIN
        self.drinks += 1
        self.mood = MOOD_CONTENT
        print(f"\nBaby drank {beverage} and has gained {ounces_to_pounds(DRINK_WEIGHT_GAIN)} lbs")
        print("\nBaby: This has quenched my thirst very well.")
        if self.drinks % 3 == 0:
            self.pee()
        self.check_burp()

    def poop(self):
        print("-Baby poops-")
        self.weight -= 5
        self.mood = MOOD_CONTENT

    def pee(self):
        print("-Baby pees-")
        self.weight -= 4
        self.mood = MOOD_CONTENT

    def laugh(self):
        print("\nHAHAHAHAHAHAHAHAHA")
        self.mood = MOOD_HAPPY

    def scream(self):
        print("\nAAAAAAAAAAAAAAAAAAAAAAHAAAAAAAAAAH!")
        self.mood = MOOD_MAD

    def cry(self):
        print("\nBaby: WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWAAAAAAAAAAAAAAAAAAA!")
        self.mood = MOOD_SAD

    def sleep(self):
        print("\n-Baby falls asleep dreaming about puppies-")
        self.mood = MOOD_CONTENT

    def burp(self):
        print("-Baby burps-")
        self.mood = MOOD_HAPPY

    def has_doubled_weight(self):
        return self.weight >= self.starting_weight * 2

    def introduce(self):
        thing = random.choice(FUNNY_THINGS)
        print(f"\nBaby: Hi! My name is {self.name}.")
        years, months = divmod(age_in_months(self.birthday), 12)
        year_text = f"{years} year{'s' if years != 1 else ''}"
        month_text = f"{months} month{'s' if months != 1 else ''}"
        print(f"I am {year_text} and {month_text} old and I weigh {ounces_to_pounds(self.weight)} lbs.")
        print(f"I really like to {thing}!")

    def display_status(self):
        print("\n--- Baby Status ---")
        print(f"Name: {self.name}")
        print(f"Birthday: {self.birthday}")
        print(f"Feedings: {self.feedings}")
        print(f"Drinks: {self.drinks}")
        print(f"Weight: {self.weight} oz")
        print(f"Weight: {ounces_to_pounds(self.weight)} lbs")
        print(f"Height: {self.height} in")
        print(f"Mood: {self.mood}")
        print("-------------------")

def ounces_to_pounds(oz):
    return round(oz / OUNCES_PER_POUND, 2)


def age_in_months(birthday):
    born = datetime.strptime(birthday, "%m/%d/%Y").date()
    today = date.today()
    months = (today.year - born.year) * 12 + today.month - born.month
    if today.day < born.day:
        months -= 1
    return max(months, 0)

def ask_number(prompt, default, cast):
    while True:
        text = input(prompt).strip()
        if text == "":
            return default
        try:
            value = cast(text)
            if value > 0:
                return value
        except ValueError:
            pass
        print(f"Please enter a positive number (or press Enter for {default}).")


def ask_birthday():
    while True:
        text = input("Birthdate (MM/DD/YYYY, blank = today): ").strip()
        if text == "":
            return date.today().strftime("%m/%d/%Y")
        try:
            age_in_months(text)
            return text
        except ValueError:
            print("Please use the format MM/DD/YYYY.")


def ask_food():
    print("\n-- Food List --")
    for number, food in enumerate(FOOD_LIST, 1):
        print(f"{number}. {food}")
    while True:
        text = input(f"Choose a food by number or name (blank = {DEFAULT_FOOD}): ").strip().lower()
        if text == "":
            return DEFAULT_FOOD
        if text.isdigit() and 1 <= int(text) <= len(FOOD_LIST):
            return FOOD_LIST[int(text) - 1]
        if text in FOOD_LIST:
            return text
        print("That food is not on the list.")


def ask_drink():
    print("\n-- Drink List --")
    for number, beverage in enumerate(DRINK_LIST, 1):
        print(f"{number}. {beverage}")
    while True:
        text = input(f"Choose a drink by number or name (blank = {DEFAULT_DRINK}): ").strip().lower()
        if text == "":
            return DEFAULT_DRINK
        if text.isdigit() and 1 <= int(text) <= len(DRINK_LIST):
            return DRINK_LIST[int(text) - 1]
        if text in DRINK_LIST:
            return text
        print("That drink is not on the list.")


def main():
    name = input("Baby name: ").strip() or "Baby"
    birthday = ask_birthday()
    height = ask_number(f"Height in inches (blank = {DEFAULT_HEIGHT}): ", DEFAULT_HEIGHT, float)
    weight = ask_number(f"Starting weight in ounces (blank = {DEFAULT_WEIGHT}): ", DEFAULT_WEIGHT, float)

    baby = Baby(name, birthday, weight, height)
    baby.introduce()

    while True:
        print("\n-- Action List --")
        print("eat, drink, laugh, cry, sleep, scream, status, home")
        action = input("Please type an action: ").strip().lower()

        if action == "eat":
            baby.eat(ask_food())
        elif action == "drink":
            baby.drink(ask_drink())
        elif action == "laugh":
            baby.laugh()
        elif action == "cry":
            baby.cry()
        elif action == "sleep":
            baby.sleep()
        elif action == "scream":
            baby.scream()
        elif action == "status":
            baby.display_status()
        elif action == "home":
            print(f"\n{baby.name} is going home.")
            break
        else:
            print(f"'{action}' is not a valid action. Choose: "
                  "eat, drink, laugh, cry, sleep, scream, status, or home.")
            continue

        time.sleep(ACTION_DELAY_SECONDS)

        if baby.weight >= baby.starting_weight * 2:
            print(f"\nCONGRATULATIONS! {baby.name} doubled their starting weight "
                  f"of {baby.starting_weight} oz!")
            break

    baby.display_status()


if __name__ == "__main__":
    main()
