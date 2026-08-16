# ============== RAISING EXCEPTIONS ==============

def main():
    pace = get_pace(miles = 26.2, minutes = 180)
    print(f'You need to run each mile in {round(pace, 2)} minutes')

def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError('Invalid value for minutes, minutes must be greater than 0') # raising your own errors, naming them, specifying an exception and attributing a text

    return minutes / miles

main()