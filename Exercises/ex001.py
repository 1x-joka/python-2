# Do a program to recommend some card games to a user based on their preferences for difficulty and the number of player they want to play with

def main():
    difficulty = input('Difficult or Casual? ').capitalize()

    if not (difficulty == 'Difficult' or difficulty == 'Casual'):
        print('Enter a valid difficulty')
        return False

    players = input('Multiplayer or Single-Player? ').title()

    # This is a logic i implemented myself, regardless of the course, if the user responds with space between the letters
    divided_list = players.split() # if it's "single-player" goes to ['Single', 'Player']
    result = "-".join(divided_list)

    if not (players == 'Multiplayer' or result == 'Single-Player'):
        print('Enter a valid number of players')
        return False

    if (difficulty == 'Difficult' and result == 'Multiplayer'):
        recommend('Poker')
    elif (difficulty == 'Difficult' and result == 'Single-Player'):
         recommend('Klondike')
    elif (difficulty == 'Casual' and result == 'Multiplayer'):
        recommend('Hearts')
    else:
        recommend('Clock') # if the difficulty's Casual and the players are Single-Player
        

def recommend(game):
    print(f'You might like {game}')

main()