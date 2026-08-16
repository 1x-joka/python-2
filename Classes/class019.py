# ============== CREATING MODULES AND PACKAGES ==============
# -> This page is for "search"

from museum.artwork import get_artworks
from museum.artists import get_artists

def main():
    artwork = input('Artwork: ').strip()
    artworks = get_artworks(query = artwork, limit = 3)
    for artwork in artworks:
        print(f'* {artwork}')

    artist = input('Artist: ').strip()
    artists = get_artists(query = artist, limit = 3)
    for artist in artists:
        print(f'* {artist}')

main()