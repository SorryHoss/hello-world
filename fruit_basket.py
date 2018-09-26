#Fruit Basket Fun with Evolve
import random
play="y"

print(".\nWhat is your Name?")
player=input("")
while play=="y":
    print("Let's play a game!\nGuess what fruit I am thinking of, "+player+"!")
    fruit=random.choice(["orange","apple","pear","peach","grape"])
    if fruit=="orange" or fruit=="apple" or fruit=="grape" or fruit=="peach":
        ana="an"
    if fruit=="pear":
        ana="a"
    answer=input("")
    answer=answer.lower()
    if answer!=fruit:
        print("Wrong.  I was thinking of "+ana+" "+fruit+".")
    else:
        print("Correct!")
    play=input("Play again? yes or no\n")
    play=play.lower()
    if play=="yes":
        play="y"