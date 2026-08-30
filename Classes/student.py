from class030 import Student

def main():
    student = get_student()
    student._house = 'Number Four, Privet Drive'
    print(student)

def get_student():
    name = input('Name: ').strip()
    house = input('House: ').strip()
    student = Student(name, house)
    return student

if __name__ == '__main__':
    main()