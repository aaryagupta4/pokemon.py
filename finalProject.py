
import random

user = "hi"
p1 = 0
amount = 0
trainerNames = ["Aarya", "Tirzah", "Jay", "Susan", "Srikriti", "Kyra"]
moveChoices = [" Flamethrower ", " Water gun ", " Tackle ", " Giga Drain ", " Ember ", " Hydro Cannon ", " Frenzy Plant ", " Cut "]
objects = []
triviaQuestions = ["Who is Ash's first Pokemon?" , "What type is the most effective against Fire?" , "What type is the effective against Grass?"]
opposing = ["Charizard", "Dragonite", "Zekrom", "Reshiram"]
money = 0

move1 = random.choice(moveChoices)
moveChoices.remove(move1)
move2 = random.choice(moveChoices)
moveChoices.remove(move2)
move3 = random.choice(moveChoices)
moveChoices.remove(move3)
move4 = random.choice(moveChoices)
moveChoices.remove(move4)


class Moves:
    def __init__(self, name, attack, pp):
        self.myName = name
        self.myAttack = attack
        self.myPP = pp

    def getName(self):
        return self.myName

    def getAttack(self):
        return self.myAttack

    def getPP(self):
        return self.myPP

    def setName(self, name):
        self.myName = name

    def setAttack(self, attack):
        self.myAttack = attack

    def setPP(self, pp):
        self.myPP = pp


class Item:
    def __init__(self, name, stat, value, cost, amount):
        self.myName = name
        self.myStat = stat
        self.myValue = value
        self.myCost = cost
        self.myAmount = 0

    def getAmount(self):
        return self.myAmount

    def getName(self):
        return self.myName

    def getStat(self):
        return self.myStat

    def getValue(self):
        return self.myValue

    def getCost(self):
        return self.myCost

    def setAmount(self, amount):
        self.myAmount = amount

    def setName(self, name):
        self.myName = name

    def setStat(self, stat):
        self.myStat = stat

    def setValue(self, value):
        self.myValue = value

    def setCost(self, cost):
        self.myCost = cost


class Player:
    def __init__(self, pokemon, label, money):
        # This will be placed in a list
        self.myPokemon = pokemon
        self.myLabel = label
        self.myMoney = 0



    def getPokemon(self):
        return self.myPokemon

    def getLabel(self):
        return self.myLabel

    def getMoney(self):
        return self.myMoney

    def setMoney(self, money):
        self.myMoney = money

    def setPokemon(self, pokemon):
        self.myPokemon = pokemon

    def setLabel(self, label):
        self.myLabel = label




class Pokemon:
    def __init__(self, speed, offense, power, level, health, defense, damage, name):
        self.mySpeed = speed
        self.myDefense = defense
        self.myOffense = offense
        self.myPower = power
        self.myLevel = level
        self.myMaxHealth = health
        self.myCurrentHealth = health
        self.myDamage = damage
        self.myName = name

    def getMaxHealth(self):
        return self.myMaxHealth

    def getCurrentHealth(self):
        return self.myCurrentHealth

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

    def getDamage(self):
        return self.myDamage

    def getName(self):
        return self.myName

    def setName(self, name):
        self.myName = name

    def setCurrentHealth(self, health):
        self.myCurrentHealth = health

    def setMaxHealth(self, health):
        self.MaxmyHealth = health

    def setDamage(self, damage):
        self.myDamage = damage

    def setSpeed(self, speed):
        self.mySpeed = speed

    def setDefense(self, defense):
        self.myDefense = defense

    def setOffense(self, offense):
        self.myOffense = offense

    def setPower(self, power):
        self.myPower = power

    def setLevel(self, level):
        self.myLevel = level


def printStats():
    global p1
    p1 = Pokemon(random.randint(10, 15), random.randint(10, 50), random.randint(10, 50), random.randint(3, 5), random.randint(10, 15), random.randint(1, 5), random.randint(10, 15), name)


charmander = False
squirtle = False
bulbasaur = False


def map():
    map1 = ["_", "_", "_", "_", "_", "_"]
    map2 = ["|", '-', 'BM', '-', "-", "|"]
    map3 = ['|', "G", '-', 'U', 'PG', '|']
    map4 = ['|', '-', '-', '-', '-', '|']
    map5 = ["|", "_", "_", "_", "_", "|"]
    print(map1[0], map1[1], map1[2], map1[3], map1[4], map1[5])
    print(map2[0], map2[1], map2[2], map2[3], map2[4], map2[5])
    print(map3[0], map3[1], map3[2], map3[3], map3[4], map3[5])
    print(map4[0], map4[1], map4[2], map4[3], map4[4], map4[5])
    print(map5[0], map5[1], map5[2], map5[3], map5[4], map5[5])


name = input("Please enter your name")
print("Hello " + name + " and welcome to Aarya's world of Pokemon!")
print("To start, let's have you pick your starter Pokemon.")
print("Your options are:")
print("Squirtle; a water type Pokemon")
print("Charmander; a fire type Pokemon")
print("And Bulbasaur; a grass type Pokemon")


def pickStarter():
    global p1
    global bulbasaur
    global charmander
    global squirtle

    starter = input("Type your choice here with 1 as Bulbasaur, 2 as Squirtle, and 3 as Charmander")
    if starter == "1":
        print("You chose the grass type, Bulbasaur. Are you sure?")
        sure = input("Please input 'YES' or 'NO' in all caps here")
        if sure == "YES":
            print("Your starter Pokemon is now Bulbasaur! He's happy to have you!")
            starter = "Bulbasaur"
            bulbasaur = True
            p1.setName("Bulbasaur")
        if sure == "NO":
            pickStarter()
    if starter == "2":
        print("You chose the water type, Squirtle. Is this your final decision?")
        sure = input("enter YES or NO in all caps here")
        if sure == "YES":
            print("Yay, you chose Squirtle! She's happy to have you!")
            starter = "Squirtle"
            squirtle = True
            p1.setName("Squirtle")
        if sure == "NO":
            pickStarter()
    if starter == "3":
        print("You chose the fire type, Charmander. Is this your final decision?")
        sure = input("enter YES or NO in all caps here")
        if sure == "YES":
            print("Nice, you chose Charmander! He's excited to see you.")
            starter = "charmander"
            charmander = True
            p1.setName("Charmander")
        if sure == "NO":
            pickStarter()
    menu()


def menu():
    map()
    print("Enter 1 to see the map key")
    choice = input("Enter 2 to access your inventory, else click anything else")
    if choice == "2":
        inventory()

    place = input("Where you would like to go? Print the corresponding keys for each place.")

    if place == "1":
        print("W = Wild Grass")
        print("U = Where you are")
        print("PC = Pokemon Center")
        print("G = Pokemon Gym")
        print("BM = Black Market")
        menu()

    if place == "BM":
        blackMarket()

    if place == "W":
        grass()

    if place == "PC":
        center()

    if place == "G":
        gym()


def grass():
    meet = False

    while meet == False:
        print("Walking through grass")
        print("...")
        print("...")
        chance = random.randint(1, 5)
        if chance == 2:
            meet = True
            encounter()


def encounter():
    global p1
    wildPokemonNames = ["Ratata", "Pidgey", "Togepi"]
    wildPokemon = Pokemon(speed=random.randint(10, 15), offense=random.randint(10, 50), power=random.randint(10, 50),
                          level=random.randint(3, 5), health=random.randint(10, 15), defense=random.randint(10, 15),
                          damage=random.randint(10, 15), name=random.choice(wildPokemonNames))
    print("Uh Oh. You ran into " + wildPokemon.getName() + ". What would you like to do?")
    runAway = input("Press 1 to battle, 2 to run.")
    if runAway == "2":
        if p1.getLevel() < wildPokemon.getLevel():
            print("You were unable to get away. You must battle")
            battle(wildPokemon)
        else:
            print("You safely got away")
            menu()
    else:
        battle(wildPokemon)


def battle(opponentPokemon):
    # The faster Pokemon goes first.
    if p1.getSpeed() > opponentPokemon.getSpeed():
        attacker = p1
        defender = opponentPokemon
    else:
        attacker = opponentPokemon
        defender = p1


    while opponentPokemon.getCurrentHealth() > 0 and p1.getCurrentHealth() > 0:
        handleTurn(attacker, defender)

        # Swap the attacker and defender
        temp = defender
        defender = attacker
        attacker = temp


def handleTurn(attackingPokemon, defendingPokemon):
    global p1
    global move1
    global move2
    global move3
    global move4
    global p1, user
    global money

    if attackingPokemon == p1:
        choice = input("What move would you like your Pokemon to do." + move1 + move2 + move3 + move4)
    else:
        choice = random.choice(moveChoices)

    print(attackingPokemon.getName() + " used " + choice + "!")

    # Calculate the damage done by the attacking Pokemon
    offense = attackingPokemon.getOffense()
    defense = defendingPokemon.getDefense()
    result = offense/defense
    power = attackingPokemon.getPower()
    product = power * result
    damage = product * random.uniform(0, 1)

    print(attackingPokemon.getName() + " did " + str(damage) + " damage to " + defendingPokemon.getName())

    # Update the defending Pokemon's health

    newHealth = defendingPokemon.getCurrentHealth() - damage
    newHealth = max(newHealth, 0)
    defendingPokemon.setCurrentHealth(newHealth)

    # Check if the defending Pokemon fainted.
    if newHealth == 0:
        print(defendingPokemon.getName() + " fainted.")
        print(attackingPokemon.getName() + " is the winner!")
        if defendingPokemon.getName() == p1.getName():
            print("You rushed to the Pokemon Center...")
            center()
        if attackingPokemon.getName() == p1.getName():
            amount = random.randint(200, 400)
            print("You collected " + str(amount) + " dollars!")
            money = amount + money
        menu()
    else:
        print(defendingPokemon.getName() + "'s health is now " + str(defendingPokemon.getCurrentHealth()))
        print(attackingPokemon.getName() + "'s health is now " + str(attackingPokemon.getCurrentHealth()))


def center():
    newHealth = 0
    print("Welcome to the Pokemon Center!")
    choice = input("Would you like to heal your Pokemon? Press 1 if you would like to, or press anything else if otherwise")
    if choice == "1":
        print("Healing your Pokemon...")
        print("...")
        print("...")
        print("...")
        print(str(p1.getName()) + "'s old health was " + str(p1.getCurrentHealth()))
        newHealth = p1.getMaxHealth()
        p1.setCurrentHealth(newHealth)
        print(str(p1.getName()) + "'s new health is now " + str(p1.getCurrentHealth()))
        print("Your Pokemon is all healed up! We hope to see you again soon! :)")
        menu()
    menu()


def gym():
    print("Welcome to the Pokemon Gym")
    question1 = random.choice(triviaQuestions)

    if question1 == triviaQuestions[0]:
        correct1 = "Pikachu"

    if question1 == triviaQuestions[1]:
        correct1 = "Water"

    if question1 == triviaQuestions[2]:
        correct1 = "Fire"

    print("Answer a question to get to your first opponent!")
    answer = input(question1)

    if answer == correct1:
        firstBattle()
    else:
        print("Incorrect. Please come back to the gym later to try again!")
        menu()





def firstBattle():
    trainerName = random.choice(trainerNames)
    print("Correct! You may now battle against the gym leader, " + trainerName)
    trainerPokemon = Pokemon(speed=random.randint(10, 15), offense=random.randint(10, 50), power=random.randint(10, 50),
                          level=random.randint(3, 5), health=random.randint(10, 15), defense=random.randint(10, 15),
                          damage=random.randint(10, 15), name=random.choice(opposing))

    trainer = Player(trainerPokemon, trainerName)
    print(trainer.getLabel() + " brought out " + trainerPokemon.getName())

    battle(trainerPokemon)






def blackMarket():
    global amount
    global money
    print("Welcome to the Black Market")
    print("We sell stat enhancing 'medicine'.")
    print("You have " + str(money) + " dollars")
    if money <= 0:
        print("Please come back with money.")
        menu()
    print("Input which medicine you would like to buy")
    choose = input("""
1: Carbos
2: Zinc
3: HP Up
4: Protein
    """)

    if choose == "1":
        item = Item(name='Carbos', stat='Speed', value=10, cost=100, amount=0)

    if choose == "2":
        item = Item(name='Zinc', stat='Defense', value=10, cost=100, amount=0)

    if choose == "3":
        item = Item(name='HP UP', stat='Health', value=10, cost=100, amount=0)

    if choose == "4":
        item = Item(name='Protein', stat='Offense', value=10, cost=100, amount=0)


    itemName = item.getName()
    stat = item.getStat()
    value = item.getValue()
    cost = item.getCost()

    print("Do you want to buy " + itemName + " ? It boosts your " + stat + " by " + str(value) + " and costs " + str(cost) + " ?")

    choice = input("Input YES or NO")
    if choice == "YES":
        print("You purchased 1 " + itemName)
        objects.append(itemName)
        amount = amount + 1
        Item.setAmount = amount
        money = Item.getCost = money
        print("You now have " + str(money) + "remaining")
        more = input("Would you like to buy more? Please input 1 if so, 2 if not.")
        if more == "1":
            blackMarket()
        else:
            menu()

    if choice == "NO":
        exit = input("Would you like to exit the shop? Enter 1 if so, else enter 2")
        if exit == "1":
            menu()
        else:
            blackMarket()


def inventory():
    print("Hello, what would you like to do?")
    print("1: My Pokemon")
    print("2: My Items")
    print("3: How To Play")
    print("4 Exit")
    choice = input("Enter your choice here")

    if choice == "1":
        see()

    if choice == "2":
        items()

    if choice == "3":
        instructions()

    if choice == "4":
        menu()


def see():
    print("Here are your Pokemon")
    nickname = p1.getName()
    print(nickname)
    print("1: Give them an item")
    print("2: Look at their stats")
    print("3: Look at their moves")
    print("4: Exit")
    choice =input("What would you like to do?")

    if choice == "1":
        give()

    if choice == "2":
        stats()

    if choice == "3":
        viewMoves()

    if choice == "4":
        inventory()


def viewMoves():
    nickname = p1.getName()
    print(nickname + "'s move's are currently" + move1 + ","+ move2 + "," + move3 + ", and " + move4)
    input("Press any key to exit")
    see()


def give():
    nickname = p1.getName()
    print("Here are your items ")
    for i in range(len(objects)):
        if len(objects) == 0:
            print("You have no items")
        print(objects[i-0])

    choice = input("What would you like to give your Pokemon? Press any key to exit")
    if choice == "Zinc":
        if "Zinc" in objects:
            oldDefense = p1.getDefense()
            newDefense = p1.getDefense() + 10
            p1.setDefense = newDefense
            print(nickname + "'s old defense was " + str(oldDefense) + " and now it's " + str(newDefense))
            objects.remove("Zinc")
        else:
            print("Sorry, you don't have Zinc.")
            give()

    if choice == "Carbos":
        if "Carbos" in objects:
            oldSpeed = p1.getSpeed()
            newSpeed = p1.getSpeed() + 10
            p1.setSpeed = newSpeed
            print(nickname + "'s old speed was " + str(oldSpeed) + " and now it's " + str(newSpeed))
            objects.remove("Carbos")
        else:
            print("Sorry, you don't have Carbos.")
            give()

    if choice == "HP UP":
        if "HP UP" in objects:
            oldHealth = p1.getMaxHealth()
            newHealth = p1.getMaxHealth() + 10
            p1.setHealth = newHealth
            print(nickname + "'s old health was " + str(oldHealth) + " and now it's " + str(newHealth))
            objects.remove("HP UP")
        else:
            print("Sorry, you don't have HP UP.")
            give()

    if choice == "Protein":
        if "Protein" in objects:
            oldOffense = p1.getOffense()
            newOffense = p1.getOffense() + 10
            p1.setHealth = newOffense
            print(nickname + "'s old offense was " + str(oldOffense) + " and now it's " + str(newOffense))
            objects.remove("Protein")
        else:
            print("Sorry, you don't have Protein.")
            give()

    see()


def stats():
    nickname = p1.getName()
    print("Here are " + nickname + "'s stats!")
    print("Speed: " + str(p1.getSpeed()) + "\n Power: " + str(p1.getPower()) + "\n level: " + str(p1.getLevel()) + "\n Health: " + str(p1.getCurrentHealth()) + "\n Defense: " + str(p1.getDefense()))
    see()


def items():
    print("Here are your items ")

    for i in range(len(objects)):
        print(objects[i-0])

    see()


def instructions():
    print("Pokemon is a complex game. What would you like to learn more about?")
    print("1: Pokemon Gym")
    print("2: Pokemon Center")
    print("3: Black Market")
    print("4: How to battle Pokemon")
    print("5: Wild Grass")
    print("6: Inventory")

    choice = input("Which would you like to learn more about?")

    if choice == "1":
        print("Gotcha! So you want to learn more about the Pokemon Gym.")
        print("The Pokemon Gym in Aarya's World of Pokemon is made up of two opponents; 1 trainer, and 1 gym leader")
        print("The Gym is basically a 'level' and the player has to beat that level")
        print("The player can beat that level by beating two opponents; one trainer and the big boss Gym Leader")
        print("To access the trainer, the player has to answer a trivia question, and if they beat the trainer, they must do the same with the Gym Leader")
        print("If the player manages to beat the Gym Leader, they earn a Random Badge")
        print("If the player loses to either the Trainer or the Leader, they are rushed to the Pokemon Center")

    if choice == "2":
        print("The Pokemon Center is a place where you can heal your injured Pokemon")
        print("The Pokemon Center restores your Pokemon back to full stats")
        print("Coming here after battling anyone is a great idea")

    if choice == "3":
        print("You are able to buy medicine here to boost your Pokemon's stats!")

    if choice == "4":
        print("Car")

    see()

def main():
    printStats()
    pickStarter()


main()