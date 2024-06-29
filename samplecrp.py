# Importing Image class from PIL module
from PIL import Image
import os

all_files = []

d="/home/pankaj/Pictures/"
def get_all_files():
    for path in os.listdir(d):
        full_path = os.path.join(d, path)
        if os.path.isfile(full_path):
            all_files.append(full_path)

def crop_image(location):
    im = Image.open(location)
    width, height = im.size
    left = 80
    top = 100
    right = width
    bottom = 740
    im1 = im.crop((left, top, right, bottom))
    filename = os.path.basename(location)
    im1.save(d+"crop_img/"+filename)

get_all_files()
print(all_files)

for file in all_files:
    crop_image(file)
