# ============== DICTIONARIES ==============


def main():
    spacecraft = {
        "name": "Voyager 1", # key = name; value = Voyager 1
        "distance": 163
    }
    spacecraft["size"] = 120 # other way to add a key in a dictionary

    spacecraft.update({ # for I add a multiple keys and values in a dictionary
        "orbit": "Sun",
        "distance_moon": 1200
    })

    print(create_report(spacecraft))

def create_report(spacecraft):
    return f'''
        ======= REPORT =======

        Name: {spacecraft.get("name", "Unknown")}
        Distance: {spacecraft.get("distance", "Unknown")} AU
        Orbit: {spacecraft.get("orbit", "Unknown")}

        ======================
    '''

# spacecraft.get("distance", "Unknown") = turn the distance's key optional, if not exists goes print "Unknown"

main()

distances = { # representing multiples dictionaries relationing name and distance of each other
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main2():
    for name in distances.keys(): # for return the keys (first column)
        print(f'{name} is {distances[name]} AU from Earth') # return the name and his respective distance

    for distance in distances.values(): # for return the values (second column)
        print(f'{distance} AU is {convert(distance)} m')

def convert(au):
    return au * 149597870700

main2()