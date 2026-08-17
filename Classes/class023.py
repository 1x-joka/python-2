# ============== FILE I/O ==============
# -> They're a way to store datas definitively on your desktop/mobile/mac/...

name = input("What's your name? ").strip()

# open() = allow us enter in the file and read the datas. We specify when the file is and how i want open

# file = open('names.txt', 'a') = I want store all the names that I write in this file who I create now. 'w' = replaces the previous content; 'a' = keeps the content and adds it at the end; 'r' = read the content

with open('name.txt', 'a') as file: # with open the file, attribute to the variable 'file'
    file.write(f'{name}\n') # writing...
    # file.close() = close and save automatically, but when we use with, it's desnecessary

# These code is equivalent do a double click in a .txt, write, save and close

# But if I execute, write and exit; execute, write and exit; The file just save the last update that I made.

with open('name.txt', 'r') as file:
    # lines = file.readlines() = the objective is read all the lines, store in a variable called 'lines'
    for line in file: # simplifying
        print(f'Hello, {line.rstrip()}') # rstrip() to removing the \n duplicate after the write and, sequencially, show me

# for the program not to print every line looked at, I want it to analyze everything, sort them and print, we have to do it another way...

names = []

# ADD
with open('names.txt') as file:
    for line in file:
        names.append(line.rstrip()) # adding one name in each line

for name in sorted(names):
    print(f'Hello, {name}')

# READ
with open('names.txt') as file:
    for line in (sorted(file)): # reads all lines, sorts them, and then iterates over them
            print(f'Hello, {line.rstrip()}')

# Making of .csv

with open('students.csv') as file:
     for line in file:
          row = line.rstrip().split(',') # splitting this line using commas (Hermione,Gryffindor)
          print(f'{row[0]} is in {row[1]}') # ex.: Hermione is in Gryffindor

# ADD

students = []

with open('students.csv') as file:
     for line in file:
          name, house = line.rstrip().split(',')
          student = {}
          student["name"] = name
          student["house"] = house
          students.append(student) # now I have collected all the students' data, and I know what their name and house are

for student in sorted(students, key = lambda student: student["name"]): # lambda = a function without a name; it takes 'student' as a parameter and returns its name. I have to specify it because the dictionary has more than one key, so I want to avoid ambiguity with 'house'
     print(f'{student['name']} is from {student['house']}')

# What if I put Hermione, Draco, and Harry on the same line, or shuffle everything?
import csv

with open('students.csv') as file:
     reader = csv.reader(file) # the objective is to read the .csv file and correctly handle commas, quotes, and other edge cases
     for row in reader:
          students.append({
            "name": row[0],
            "house": row[1]
          })

for student in sorted(students, key = lambda student: student["name"]):
     print(f"{student['name']} is from {student['house']}")