from PIL import Image, ImageFilter

# img = Image.open('./Pokedex/pikachu.jpg')

# img.show()

# filtered_img = img.filter(ImageFilter.BLUR)

# filtered_img.save("blured_pikachu.png", 'png')

# filtered_img.show()

# filtered_img_2 = img.convert('L')

# filtered_img_2.save("black_and_white_pikachu.png", 'png')

# filtered_img_2.show()

# custom_img = img.rotate(180)

# custom_img.save("rotated_pikachu.png", 'png')

# custom_img.show()

# custom_img_2 = img.resize((300, 300))

# custom_img_2.save("resized_pikachu.png", 'png')

# custom_img_2.show()

# box = (100,100,400,400)
# region = img.crop(box)
# region.save("cropped.png", 'png')

# region.show()


# # print(img)
# # print(img.format)
# # print(img.size)
# # print(img.mode)


img = Image.open('./Pokedex/astro.jpg')
new_img = img.resize((400,400))
new_img.save("resized_astro.jpg")

img.thumbnail((400,400))
img.save("thumbnail_astro.jpg")

print(img.size)