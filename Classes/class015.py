# ============== HANDLING EXCEPTIONS ==============

distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input('Enter a spacecraft: ').strip()

    try:
        au = float(distances[spacecraft]) # trying to convert the number in front of the key to a float, because it's a string
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return
    except KeyError:
        print(f"The spacecraft '{spacecraft}' doesn't exists in my dictionary")
        return
    
    m = convert(au)
    print(f'{m} m away')

def convert(au):
    return au * 149597870700

main()