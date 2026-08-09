# ============== FUNÇÕES E VARIÁVEIS ==============

# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from str
name = name.strip()

# Capitalize user's name
name = name.capitalize() # The first letter's name stay upper and the ramainder lower

name = name.title() # The first letter's name in the all sentence stay upper

# Putting it all together
name = input("What's your name? ").strip().title()

# Say hello to user
print(f'Hello, {name}')

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2) # rounded the value of the x y calculation to 2 decimals places

# Other way...

print(f'{z:.2f}')

def hello(to = 'world'): # if nothing is filled in, it will say 'World'
    print('Hello,', to)

hello() # if empty it will say 'World'
name = input("What's your name? ")
hello(name) # you must enter your name, or nothing will appear

def main():
    name2 = input("What's your name? ")
    hello2(name2)

def hello2(name2):
    print('Hello, ', name2)

main()