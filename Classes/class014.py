# ============== DEBUGGING ==============

def main():
    height = int(input('Height: '))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print('#' * (i + 1)) # build the pyramid with a defined height

if (__name__ == '__main__'): # Python has a special variable called "__name__", when this file's executed directly, gets the value "__main__" automatically. So, if this program is executed at here, execute main()
    main()