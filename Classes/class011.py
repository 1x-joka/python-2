# ============== TUPLES ==============

import sys

def main():
    latitude = 42.367
    longitude = -71.115
    coordinates_tuple = (latitude, longitude)

    print(coordinates_tuple)
    print(f'Latitude: {coordinates_tuple[0]}')
    print(f'Longitude: {coordinates_tuple[1]}')

    print('-' * 15)

    coordinates_list = [42.367, -71.115]
    latitude2, longitude2 = coordinates_list

    print(coordinates_list)
    print(f'Latitude: {latitude2}')
    print(f'Longitude: {longitude2}')
    print(f'Size of latitude: {sys.getsizeof(latitude2)} bytes')
    print(f'Size of longitude: {sys.getsizeof(longitude2)} bytes')

    print('-' * 15)

    print(f'Size of Tuple: {sys.getsizeof(coordinates_tuple)} bytes')
    print(f'Size of List: {sys.getsizeof(coordinates_list)} bytes')

    # A tuple takes up fewer bytes containing the same amount of data. So, "when do I have to use tuple?" Simple, when you are very sure that you won't be changing the datas contained in the tuple

    # With a small software (like ours) don't a big difference, but when you think about a large software with millions and millions of rows, this can be affected

    # Tuples are ordered and immutable collections. We should use them when we have a data set that does not need to be changed

main()