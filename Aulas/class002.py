# ============== CONDITIONALS ==============

x = int(input("What's x? "))
y = int(input("What's y? "))

if (x < y):
    print('x is less than y')
elif (x > y):
    print('x is grater than y')
else:
    print('x is equal to y')

if (x < y) or (x > y):
    print("x isn't equal to y")
else:
    print('x is equal to y')

score = int(input('Score: '))

if (score >= 90) and (score <= 100): # if (90 <= score <= 100)
    print('Grade: A')
elif (score >= 80) and (score < 90):
    print('Grade: B')
elif (score >= 70) and (score < 80):
    print('Grade: C')
elif (score >= 60) and (score < 70):
    print('Grade: D')
else:
    print('Grade: F')

def main():
    z = int(input("What's z? "))
    if (is_even(z)):
        print('Even')
    else:
        print('Odd')
    
def is_even(n):
    if (n % 2 == 0):
        return True
    else:
        return False
    
    # Other way more simplified: return True if n % 2 == 0 else False

main()

name = input("What's your name? ").strip().title()

if (name == 'Harry'):
    print('Gryffindor')
elif (name == 'Hermione'):
    print('Griffindor')
elif (name == 'Ron'):
    print('Griffindor')

# if (name == 'Harry' or name == 'Hermione' or name == 'Ron')

elif (name == 'Draco'):
    print('Slytherin')
else:
    print('Who?')

match name:
    case 'Harry':
        print('Gryffindor')
    case 'Hermione':
        print('Gryffindor')
    case 'Ron':
        print('Gryffindor')
    
    # case 'Harry' | 'Hermione' | 'Ron':
        # print('Gryffindor')

    case 'Draco':
        print('Slytherin')
    case _: # for other answer
        print('Who?')