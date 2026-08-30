# ============== OBJECT-ORIENTED PROGRAMMING ==============

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f'{self.name} from {self.house}'
    
    @classmethod
    def get(cls):
        name = input('Name: ')
        house = input('House: ')
        return cls(name, house)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Missing Name!')
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError('Invalid House!')
        self._house = house

import random

houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

@classmethod
def sort(name):
    print(name, 'is in', random.choice(houses))

sort('Harry')

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError('Missing Name')
        self.name = name

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard('Albus')
student = Student('Harry', 'Gryffindor')
professor = Professor('Severus', 'Defense Against the Dark Arts')

class Vault:
    def __init__(self, galleons, sickles, knuts):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f'{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts'
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
    
potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)