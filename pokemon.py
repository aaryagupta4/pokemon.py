# Comment code out and explain how it works what each function does, ect.

import random
import math
battle = "hello"
charmander = False
squirtle = False
bulbasaur = False


class Moves:
    def __init__(self, speed, power, accuracy, health):
        self.mySpeed = speed
        self.myPower = power
        self.myAccuracy = accuracy
        self.myHealth = health


    def getSpeed(self):
            return self.mySpeed

    def getPower(self):
        return self.myPower

    def getAccuracy(self):
        return self.myAccuracy

    def getHealth(self):
        return self.myHealth

def createMoves():
    p3 = Moves(random.randint(1,5), random.randint(1,5), random.randint(80,100), random.randint(1,5))
    print("Speed: " + str(p3.getSpeed()) + "\n Power: " + str(p3.getPower()) + "\n Accuracy: " + str(p3.getAccuracy()) + "\n Health: " + str(p3.getHealth()))
    return p3

# this code is assigning variables to "stats" in other words, deciding the stats of the move
# WE do this using Classes, and we first set the stats that we'll be using in the self function
# we then set the stats/variables and assign them a self definition which will then be
# assigned a variable in a def by using random integers
# This is later shown in the print function with assigning the variables random numbers from 1, 5, and then printing it
# In this case, we are deciding the stats of any wild pokemon, but the same thing can be applied to any of the other two Class functions I have
# Specifically, the self function in my stats allows ys ti access the attributes of the class, in other words, it binds the attributes with the given arguments

class Wild:
    def __init__(self, speed, defense, offense, power, level, health):
        self.mySpeed = speed
        self.myDefense = defense
        self.myOffense = offense
        self.myPower = power
        self.myLevel = level
        self.myHealth = health
    def changeWildHealth(self, num):
        self.health -= num

    def getSpeed(self):
        return self.mySpeed

    def getDefense(self):
        return self.myDefense

    def getOffense(self):
        return self.myOffense

    def getPower(self):
        return self.myPower

    def getLevel(self):
        return self.myLevel

    def getHealth(self):
        return self.myHealth



def createWild():
    p2 = Wild(random.randint(1,5), random.randint(1,5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(10,15))
    print("Speed: " + str(p2.getSpeed()) + " \n Defense: " + str(p2.getDefense()) + " \n Offense: " + str(p2.getOffense()) + " \n Power: " + str(p2.getPower()) + " \n Level: " + str(p2.getLevel()) + " \n Health: " + str(p2.getHealth()))
    return p2



class Squirtle:
    def __init__(self, speed, defense, offense, power, health):
        self.mySpeed = speed
        self.myDefense = defense
        self.myOffense = offense
        self.myPower = power
        self.myHealth = health

    def getpPower(self, nump):
        self.getpPower -= nump

    def getSpeed(self):
         return self.mySpeed

    def getDefense(self):
        return self.myDefense

    def getOffense(self):
        return self.myDefense

    def getPower(self):
        return self.myPower

    def getHealth(self):
        return self.myHealth

def createSquirtle():
    p1 = Squirtle(random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(10, 15))

    print(" Speed: " + str(p1.getSpeed()) + "\n Power:  " + str(p1.getPower()) + "\n Offense:  " +str (p1.getOffense()) + "\n Defense:  " + str(p1.getDefense()) + "\n Health: " + str(p1.getHealth()))

    






# this is my introduction, I get crucial globals from this code which I will then use later on in my project

name = input("what would you like to go by?")
print("Hello" + name + ", and welcome to Aarya's world of Pokemon!")
print("To start, let's have you pick your starter Pokemon in the world of Kanto. Your options are Bulbasaur, Charmander, and Squirtle.")
print("PLease type out which starter you like!")


# This is the actual introduction def
# Here we get the pokemon that the user wants to use for the beginning phases of the game
# In other words, the user decides their starter pokemon through a series of if statements

def intro():
    global bulbasaur
    global charmander
    global squirtle

    starter = input("type your choice here with 1 as Bulbasaur, 2 as Squirtle, and 3 as Charmander")
    if starter == "1":
        print("you chose the grass type, Bulbasaur. This is the Pokemon that will guide you throuhout the rest of the game, are you sure you want Bulbasaur?")
        sure = input("Please input 'YES' or 'NO' in all caps here")
        if sure == "YES":
            print("Your starter pokemon is now Bulbasaur! He's happy to have you!")
            starter = "Bulbasaur"
            bulbasaur = True
        if sure == "NO":
            intro()
    if starter == "2":
        print("you chose the water type, Squirtle. Is this your final decision?")
        sure = input("enter YES or NO in all caps here")
        if sure == "YES":
            print("Yay, you chose Squirtle! She's happy to have you!")
            starter = "Squirtle"
            squirtle = True
        if sure == "NO":
            intro()
    if starter == "3":
        print("You chose the fire type, Charmander. Is this your final decision?")
        sure = input("enter YES or NO in all caps here")
        if sure == "YES":
            print("Nice, you chose Charmander! He's excited to see you.")
            starter = "charmander"
            charmander = True
        if sure =="NO":
            intro()
    print("Ready!")
    menu()



# Have an option that explans whether or not they want to know how to play, if true then list instructions, if false, don't list instructions

# This is the menu
# What the user will keep coming back to, the most important part of this game, it decides what the user wants to do and sets other functions in action
def menu():
    print("below is your menu. please enter the number corresponding on what to do.")

    where = input("""""
        1: Pokemon Center
        2: Pokemon Gym
        3: Wild Grass
        4: How to Play
        5: My Pokemon
        """"")

    if where == "1":
        center()
    if where == "2":
        gym()
    if where == "3":
        grass()
    if where == 4:
        play()
    if where == "5":
        pokemon()





# This is the Pokemon center
# Pokemon's health gets restored to the variable it used to be; ie; a pokemon took damage and is now at 50 health, the pokemon center will restore them to 100
def center():
    print("Welcome to the Pokemon Center!")
    print(str(p1.getHealth()))
    new = 0
    new = old
    print(new)

    menu()

# Gym code option from menu
# Write more how it works after you code the battle sequence

def gym():
    print("Welcome to the Pokemon Gym!")
    menu()
# the wild grass function
# A random pokemon appears and you battle it
def grass():
    global Bulbasaur
    global Charmander
    global Squirtle

    print("You are now in the territory of the pokemon. Tread carefully")
    events = [1, 2, 3]
    wild = ["Pikachu", "Ratata", "Pidgey"]

    choice = random.choice(events)
    #if choice == 1:
    print("Oh no! You've been spotted by a wild Pokemon. It's time to battle")
    battle = random.choice(wild)
    print(battle + " is your opponent")
    print("stats:")
    createWild()

    if bulbasaur == True:
        print("Bulbasaur is your Pokemon")

    if charmander == True:
        print("Charmander is your Pokemon")

    if squirtle == True:
        print("Squirtle is your Pokemon")

    battleChoices()



# Move menu for player's pokemon, currently in an array but change to classes later after your finish the rough sketch
# Creating a menu for player's moves
# Different menus for each starter Pokemon

def battleChoices():
    choice = input("""
                   1: Battle
                   2: Run
                   3: Throw a Pokeball
                   """) #a menu for what the player wants to do, whether they want to battle, run away, or capture the pokemon

    if choice == "1":
        SquirtleMove()
    if choice == "2":
        print("You successfully ran away")
        menu()
    if choice == "3":
        print("You have no Pokeballs to throw")
        ]

def SquirtleMove():
    print("move list:")
    move = input(""""
        1: water gun
        2: tackle
        3: bubble 
        4: Tail Whip
        """"")

    movea = "watergun"
    moveb = "tackle"
    movec = "bubble"
    moved = "tailwhip"

    if move == "1":
        move1()

    return movea, moveb, movec, moved

def move1():
    createMoves()
    #later turn squirtle into a variable, the variable squirtle =true thing so it can be used with all pokemon an I don't have to use multiple definitions
    print(str(p2.changeHealth(p1.getPower))) #figure out conversion from power to how much is subtracted from health



    #menu()

def play():
    print("Here's how you play!")
    menu()
# This is where you can see your pokemon, and later, perhaps interact with them
def pokemon():
    global bulbasaur
    global charmander
    global squirtle
    print("hello")
    pokemon = []
    if charmander == True:
        pokemon.append("charmander")
    if bulbasaur == True:
        pokemon.append("bulbasaur")
    if squirtle == True:
        pokemon.append("squirtle")
    print(pokemon)
    createSquirtle()

    print(str(pokemon) + " is your only current pokemon!")
    menu()

def main():
    intro()
    #menu()

main()

