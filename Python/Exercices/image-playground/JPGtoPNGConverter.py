import sys
import os
from PIL import Image


# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(image_folder, output_folder)

# check is JPG_pics/ exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through Pokedex, 
# convert images to png
# save to JPG_pics folder
for each_img in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{each_img}')
    remove_extention = os.path.splitext(each_img)[0]
    img.save(f'{output_folder}{remove_extention}.png', 'png')
    print('All done!')
