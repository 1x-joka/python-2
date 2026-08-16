# ============== API CALLS ==============

import requests

def main():
    print('Search the Art Institute of Chicago!')
    artist = input('Artist: ').strip()

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist} # searching for the artist
        )
        response.raise_for_status() # checking her status, if it's okay, it's 200
    except requests.HTTPError:
        print("Couldn't complete request!")
        return

    content = response.json() # transforming API content through the JSON format for visualization
    for artwork in content["data"]: # content["data"] = list of works
        print(f'* {artwork["title"]}') # it's a dictionary representing one work

main()