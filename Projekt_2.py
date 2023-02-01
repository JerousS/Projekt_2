"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jaroslav Shanel
email: jarekshanel@gmail.com
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

print(random_number)
guess = ""
while guess != random_number:
    guess = input()
    

    

    
