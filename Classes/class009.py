# ============== LIST METHODS ==============

def main():
    history = []

    while True:
        action = input('Action: ').strip().lower()

        if (action == 'undo'):
            undone = history.pop() # removing the last element in list
            print(f'Undone: {undone}') # show the element who is removed
        elif (action == 'restart'):
            history.clear()
        else:
            history.append(action)

        print(history) # show us the actually state of the list

main()