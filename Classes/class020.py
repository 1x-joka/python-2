# ============== RANDOM ==============
import random

cards = ['jack', 'queen', 'king']

def main():
    random.seed(0) # defines a starting point for random generation, so the same sequence can be reproduced. It's randomness who can be reproduced

    print(random.choice(cards)) # chooses 1 element
    print(random.choices(cards)) # chooses 1 element but allows repeats
    print(random.choices(cards, k = 2)) # chooses 2 elements
    print(random.sample(cards, k = 2)) # will select without replacement, that is, without being the same
    print(random.choices(cards, weights = [100, 0, 0], k = 3)) # defines the probability of choosing each card: 100% for jack and 0% for queen and king

main()