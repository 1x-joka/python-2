# ============== STRING SLICING ==============

def main():
    phone = '617-495-1000'

    print(phone)
    print(phone[0:3]) # the terminal displays the first number (index zero), second and third, just. 
    print(phone[:3]) # same thing as above but simplified
    print(phone[8:12]) # displays the eighth number until the twenty
    print(phone[8:]) # displays the eight until the final

    phone2 = '+1 617-495-1000'
    without_space = ''.join(phone2.split()) # removing all  whitespaces

    print(phone2[-4:]) # displays the fourth, backwards, until the final
    print(phone2[:3]) # considers the space too
    print(without_space[:3])

main()