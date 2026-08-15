# ============== FOR LOOPS ==============
# -> is great when you know how many times you want to iterate or you want to do something for each person or each thing you have in some list

def main():
    # print(write_letter('Yoshi', 'Princess Peach')) -> if I want repeat this 1000x ? Use "for loop"

    names = ['Yoshi', 'Mario', 'Luigi', 'Daisy', 'Bowser']

    for i in range(0 - len(names)):
        print(f"{names[i]} = {i + 1} person in Peach's List") # person respective for her "i"
        print(write_letter(names[i], 'Princess Peach')) # now we know all the names in Peach's List, we invited for respective person
    
    # Here we can't put his respective position in list
    for name in names:
        print(write_letter(name, 'Princess Peach'))

def write_letter(receiver, sender):
    return f'''
    Dear {receiver},

    You're cordially invited to a ball at
    Peach's Castle this evening, 7:00 PM.

    Sincerely,
    {sender}
    '''

main()