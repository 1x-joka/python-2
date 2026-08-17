# ============== READING AND WRITING CSVs ==============

import csv
import numpy as np #
from PIL import Image

def main():
    with open('views.csv', 'r') as views, open('analysis.csv', 'w') as analysis:
        # Taking the data of brightness

        reader = csv.DictReader(views) # read each one line like a dictionary
        for row in reader:
            # print(row["id"]) = reading only the id's
            brightness = calculate_brightness(f"row['id'].jpeg")
            print(round(brightness, 2))
        
        # Inputing this on a new file .csv

        writer = csv.DictWriter(analysis, fieldnames = reader.fieldnames + ["brightness"]) # fieldnames = what is writing on the header on top of the file; Adding one more item on header = brightness
        writer.writeheader() # write the fact

        for row in reader:
            row["brightness"] = calculate_brightness(f"row['id'].jpeg")
            writer.writerow(row)

            # brightness = calculate_brightness(f"row['id'].jpeg")
            # writer.writerow( = creating what on the header on a dictionary
                # {
                    # "id": row["id"],
                    # "english_title": row["english_title"],
                    # "japanese_title" : row["japanese_title"],
                    # "brightness": round(brightness, 2)
                # }
            # )

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
        return brightness

main()