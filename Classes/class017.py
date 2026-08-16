# ============== RAISING EXCEPTIONS ==============

import random

print(random.choice(['Heads', 'Tails'])) # randomly choosing an element from the list

coin = random.randint(1, 10) # randomly sorting a number between 1 and 10
print(coin)

cards = ['Jack', 'Queen', 'King']
random.shuffle(cards) # shuffing all the elements from the list
for card in cards:
    print(card)

from statistics import mean

print(mean([100, 90])) # taking the number that is exactly halfway through this range

from sys import argv, exit # argv = allows us taking what we write in front of the command line and input in our program (python class017.py [write here]); exit = allows us exit the program

if (len(argv) < 2):
    exit('Too few arguments!') # write and, after, exit
elif (len(argv) > 2):
    exit('Too many arguments!')

print(f'Hello, my name is {argv[1]}')

for arg in argv[1:-1]: # print the last name
    print(f'Hello, my name is {arg}')

from sayings import hello
if (len(argv) == 2):
    hello(argv[1])