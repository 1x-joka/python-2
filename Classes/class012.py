# ============== WHILE LOOP ==============
from soil import sample # a library who the professor made in another program or other programs

def main():
    moisture = sample()
    days = 0
    print(f'Moisture is {moisture}%')

    while (moisture > 20): # while the moisture's percent is less than 20% the program goes show the code...
        moisture = sample()
        days += 1
        print(f'Day {days}: Moisture is {moisture}%')
    
    print('Time to water!') # when the percent is greater than, or equal, a 20%

main()