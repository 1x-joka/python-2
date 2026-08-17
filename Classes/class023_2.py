import csv

students = []

with open('students2.csv') as file:
    reader = csv.DictReader(file) # to analyze the rows as a dictionary ("name": name, "house": house), I have to define the names of the columns in the first line of the .csv file
    for row in reader:
        students.append({
            "name": row["name"],
            "house": row["house"]
        })

    # This is good because if someone changes the order of the columns in students.csv, I only need to change the header, and my Python code already accounts for that because the row is accessed by its column name. This is called defensive programming

for student in sorted(students, key = lambda student: student["name"]):
    print(f'{student['name']} is from {student['house']}')

name = input("What's your name? ").strip()
house = input("What's your house? ").strip()

with open('students3.csv', 'a') as file:
    writer = csv.writer(file) # writes to the .csv file using this library
    writer.writerow([name, house]) # automatically writes the values in the order defined here