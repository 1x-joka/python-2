# ============== LOOPS ==============

i = 3
while (i != 0):
    print('meow') # three times
    i -= 1

for item in [0, 1, 2]: # for once item in list what have 3 items
    print('meow') # three times

for _ in range(3): # for the cases who are too extended (1 million, to example)
    print('meow') # three times

print('meow\n' * 3, end = "")

while True:
    n = int(input("What's n? "))
    if (n > 0):
        break

for _ in range(n): # the last number in "n" who i put
    print('meow') # "n" times


def main():
    number = get_number() # catch the number who the user digits
    meow(number) # print "number" meow's

def get_number():
    while True:
        n2 = int(input("What's n? "))
        if (n2 > 0):
            break
    return n2 # for the input in top

def meow(n2):
    for _ in range(n2):
        print('meow')
    
main()

students = ['Hermione', 'Harry', 'Ron', 'Draco']
houses = ['Gryffindor', 'Gryffindor', 'Gryffindor', 'Slytherin']

for i in range(len(students)): # for the once item in list... (we have put "len" because inside on a list only accept numbers)
    print(i + 1, students[i]) # put the index and the respective name

students2 = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin"
}

print(students2['Hermione']) # print in the screen who Hermione's house

for student in students2:
    print(student) # return me the name for all people
    print(student, students2[student], sep=", ") # return me all people and his respective house

students3 = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter"
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack-Russel Terrier"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None # None = absence of a value
    }
]

for student2 in students3:
    print(student2["name"]) # return me his/her name
    print(students2["house"])