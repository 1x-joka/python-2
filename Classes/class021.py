# ============== UNIT TESTS ==============
# -> to testing your code using code of your own

# This program's name is "calculator"

def main():
    x = int(input("What's x? "))
    print(f'x squared is {square(x)}')

def square(n):
    return n * n # if i changed this calculation, it will give error in "test_calculator" because "assert" verified if 3 squared is 9, if yes, it ignores in silence, if not, give error

if (__name__ == '__main__'):
    main()