# ============== PILLOW ==============

from PIL import Image, ImageFilter

def main():
    with Image.open('name.jpeg') as img:
        print(img.size)
        print(img.format)
        img = img.rotate(180)
        img.filter(ImageFilter.BLUR) # applying the blur on image
        img.save('new.jpeg')

main()