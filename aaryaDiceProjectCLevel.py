import random
import math

total = 0
nofrr = 0
players = []
turnIndex = 0
totals = [0, 0, 0]
numRerolls = [0, 0, 0]

def intro():
    print("hello")
    global total
    global players
    p1 = input("Hello and welcome to Aarya's Game of Dice! Please enter Player 1's name")
    p2 = input("Enter Player 2's here")
    p3 = input("Enter Player 3's here")
    print("Player 1: " + p1 + " Player 2: " + p2 + " Player 3: " + p3)

    players = [p1, p2, p3]
    print(players)



    # for multiplayer, we would have the same function running for each player except without the "would you like to play again"
    #

def dice():
    global turnIndex
    global totals
    global numRerolls
    global total
    global players
    turn = True
    print("it's " + players[turnIndex] + "'s turn!")

    print("Here are your rolls in order:")

    rolls = []
    for i in range(5):
        rolls.append(random.randint(1, 6))
        print("dice " + str(i+1) + ": " + str(rolls[i]))

    if totals[turnIndex] >= 50:
        end()

    ans = input("Would you like to re roll? Please enter 1 if yes and 2 not")
    if ans == "1":
        reroll(rolls)
    else:
        almost(rolls)



    return rolls



def reroll(rolls):
    global turnIndex
    global numRerolls
    global nofrr
    global total
    index = input("what number dice would you like to re roll?")
    index = int(index)
    rolls[index - 1] = random.randint(1, 6)
    nofrr = nofrr + 1
    numRerolls[turnIndex] = nofrr
    # number of re rolls

    print(rolls)
    if numRerolls[turnIndex] == 2:
        print("That was your last roll!")
        almost(rolls)

    if totals[turnIndex] >= 50:
        end()
    ans = input("would you like to re roll? input 1 if yes, otherwise input 2")
    if ans == "1":
        reroll(rolls)
    if ans == "2":
        almost(rolls)



def end():
    global total
    global totals
    print("thanks for playing!")
    print("the winner was " + players[turnIndex] + " with the score of: " + str(max(totals)))
    print("your final scores are:")
    print("Player 1:" + str(totals[0]))
    print("Player 2:" + str(totals[1]))
    print("Player 3:" + str(totals[2]))



    exit()

def almost(rolls):
    global turnIndex
    global total
    global totals
    global nofrr
    global players


    score = sum(rolls)
    total = score
    totals[turnIndex] = total + totals[turnIndex]
    print("your total score is now: " + str(totals[turnIndex]))
    total = 0
    if totals[turnIndex] >= 50:
        end()
    else:
        turnIndex = turnIndex + 1
        if turnIndex == 3:
            turnIndex = 0
        dice()












def main():
    global players
    intro()
    dice()




if __name__ == "__main__":
    main()