# ============== CAPTURE GROUPS ==============
import re

locations = {
    "+1": "United States and Canada",
    "+62": "Indonesia",
    "+505": "Nicaragua"
}

def main():
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}" # (?P<name>...) = creates a named capture group; \+ = literal +; \d = any digit; {1,3} = between 1 and 3 digits; \d{3} = 3 digits; - = literal hyphen; \d{4} = 4 digits
    number = input('Number: ')

    match = re.search(pattern, number)
    if match:
        country_code = match.group("country_code") # .group("country_code") = shows exactly what was captured by the group named "country_code"
        print(locations[country_code])
    else:
        print('Invalid')
    
main()