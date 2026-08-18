# ============== PATTERNS ==============

# Format of code's hexadecimals: #(qtd red)(qtd green)(qtd blue)
# red = #FF0000
# green = #00FF00
# blue = #0000FF
# white = #FFFFFF -> all the colors together
# black = #000000 -> ausence of colors

import re

def main():
    code = input('Hexadecimal color code: ').strip()
    
    pattern = r"^#[a-fA-F0-9]{6}$" # r = raw string; {6} = I wait these especifically characteres in quantifier; a - f = a from b; ^ = when i search for this default, it's obligatorily #
    match = re.search(pattern, code) # saving the color found

    if match: # if I found the color
        print(f'Valid. Matched with {match.group()}') # .group() = mostrará exatamente o que o 'search' encontrou como uma correspondência
    else:
        print('Invalid')
main()