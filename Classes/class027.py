# ============== REGULAR EXPRESSIONS (RegEX) ==============

import re

email = input("What's your email? ").strip()

if re.search(r".*@.+", email): # zero or more characters, followed by a literal @ sign, followed by one or more characters
    print('Valid')
elif re.search(r".+@.+\.edu", email): # ex.: harvard@harvard.edu
    print('Valid')
elif re.search(f"^[^@]+@.+\.edu$", email): # starts with one or more characters that are not @, followed by a literal @ sign, followed by one or more characters and ending with .edu
    print('Valid')
elif re.search(f"^[a-zA-Z0-9_]+@[^@]+\.edu$", email): # starts with one or more letters, numbers or underscores, followed by @, followed by one or more characters that are not @ and ending with .edu
    print('Valid')
elif re.search(f"^\w+@\w+\.edu$", email, re.IGNORECASE): # starts with one or more word characters, followed by @, followed by one or more word characters and ending with .edu, ignoring uppercase and lowercase differences
    print('Valid')
elif re.search(f"^\w+@(\w\.)?\w+\;edu$", email, re.IGNORECASE): # starts with one or more word characters, followed by @, optionally followed by a word character and a dot, followed by one or more word characters and ending with ;edu, ignoring uppercase and lowercase differences
    print('Valid')
else:
    print('Invalid')

name = input("What's your name? ").strip()

matches = re.search(r"^(.+), *(.+)$", name)

if matches:
    last, first = matches.groups() # groups put the sentences together
    name = f"{first} {last}"

    name = matches.group(2) + " " + matches.group(1) # group 1 is last and group 2 is first

print(f'Hello, {name}')

url = input('URL: ').strip()
username = url.replace('https://youtube.com/', "") # removes the exact 'https://youtube.com/' text from the URL
username = url.removeprefix('https://youtube.com/', "") # removes 'https://youtube.com/' only if it appears at the beginning of the URL
username = re.sub(r"https://youtube.com/", "", url) # searches for 'https://youtube.com/' using a regular expression and replaces it with nothing
username = re.sub(r"^(https?://)?(www\.)?youtube\.com/", "", url) # optionally matches http:// or https://, optionally matches www., followed by youtube.com/ and replaces the entire match with nothing
print(f'Username: {username}')

username = re.sub(r"^https?://(www\.)?youtube\.com/(.+)$", url) # matches an http or https YouTube URL, optionally with www., captures everything after youtube.com/ and replaces the entire match with the value of url

if matches:
    print(f'Username: {matches.group(1)}') # prints the text captured by the first group of the previous regular expression match
re.search() # searches for a pattern inside a string and returns a Match object if the pattern is found, otherwise returns None