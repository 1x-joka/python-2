# ============== DICTIONARY METHODS ==============
# -> function you can use to manipulate your dictionary in Python

words = {
    "pair": 4,
    "hair": 4,
    "chair": 5,
    "graphic": 7
}

def main():
    print('Welcome to Spelling Bee!')
    print('Your letters are: A I P C R H G')
    print('=-' * 16)

    for word, value in words.items():
        print(f'{word} was worth {value} points')
        # words.items() -> return me the key and his respective value associate with her
    print('=-' * 16)

    while (len(words) > 0): # how many keys in 'words'
        print(f'{len(words)} words left!')
        guess = input('Guess a word: ').strip().lower()

        # TODO: Check if guess in dictionary
        if (guess in words.keys()):
            points = words.pop(guess) # removing the word who I write in the dictionary
            print(f'God job! You scored {points} points')
            print('=-' * 16)

            # if I put words.pop without a variable, it's going an error, therefore I add in variable how many words I got it right (- 1 word available)
        else:
            print('Try again :(')
            print('=-' * 16)

        if (guess == 'graphic'): # I put after the above code to avoid errors, such as: You've won and Try Again even if you got ir right
            words.clear() # cleaning all of the keys
            print("You've won!")
            print('=-' * 16)
    
    print("That's the game!") # when not more keys in dictionary

main()