import sys
from PIL import Image

images = [] # accumulating all the images provided in the command line

for argument in sys.argv[1:]: # each image provided in the command line; [1:] skips the program name and takes all the remaining arguments
    image = Image.open(argument) # opening the image and giving me functionalities to manipulate it
    images.append(image) # adding the images to the list to form the GIF

images[0].save( # saving the first image to the disk
    "costumes.gif",
    save_all=True,
    append_images=images[1:],
    duration=200,
    loop=0
    # saving the animation in a single file called costumes.gif;
    # images[1:] = appending all the remaining images to the first one,
    # creating the animation; duration = 200 milliseconds between each frame;
    # loop = 0 means the animation repeats infinitely
)