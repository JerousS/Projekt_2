"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jaroslav Shanel
email: jarek.shanel@gmail.com
discord: JaroslavS
"""
import random
oddelovac = "-----------------------------------------------"
print("Hi there!", oddelovac, sep="\n")
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print(oddelovac, "Enter a number", oddelovac, sep="\n")
number = []
while len(number) !=4:
    i=random.randint(0,9)
    if i not in number:   
        number.append(i)
    if number[0] == 0:
        number.remove(0)
random_number = "".join([str(i) for i in number])
hr = []
print(random_number)
guess = ""
num_of_guesses = 0
while guess != random_number:
    guess = input()
    hr.clear()
    num_of_guesses+=1
    if len(guess) != 4 or str(guess[0]) == "0" or not guess.isnumeric():
        print("Please put 4digit number not starting with 0")
        continue
    for i in str(guess):
        if not i in hr:
            hr.append(i)
        else:
            print("4digit number with no duplicites please")
            break
    else:
        bull = 0
        cow = 0
        for i in range(4):
            if guess[i] == random_number[i]:
                bull+=1
            elif guess[i] in random_number:
                cow+=1
        print(bull, "bulls" if bull > 1 else "bull",",", cow, "cows" if cow>1 else "cow")
        print(oddelovac)
else:
    print("Correct, you've guessed the right number in",num_of_guesses, "guesses!")    