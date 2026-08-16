# ============== EXCEPTIONS ==============

def main():
    get_intx()

    y = get_inty()
    print(f'y is {y}')

def get_intx():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x isn't an integer")
        else: # if x haven't an error...
            print(f'x is {x}')
            break

def get_inty():
    while True:
        try:
            return int(input("What's y? "))
        except ValueError:
            pass # don't repeat the sentence, just continue to the next condition. Pass isn't, literally, "pass to the next condition" but means "don't execute any action at this point"
    
    # pass != continue: continue says "skip the rest of this iteration and goes to the next" and pass says "don't execute anything"
    # pass != break: break says "kick out of the loop!"
        
main()