from PIL import Image

# img = Image.open("pencils.jpg")

# img.crop((0,0,100,100))

# img.show()

# Exercise
words = Image.open("word_matrix.png")
mask = Image.open("mask.png")

mask = mask.resize(words.size)
mask.putalpha(200)

words.paste(mask, (0,0), mask)

words.show()
mask.show()