from PIL import Image, ImageDraw
import random

img = Image.new('L', (70,70))

draw = ImageDraw.Draw(img)


p1 = (random.randint(3, 30), random.randint(3, 30))
p2 = (random.randint(30, 68), random.randint(30, 68))

draw.rectangle((p1, p2), outline=255)
draw.arc((p1, p2), 0, 360, fill=255)

del draw

img.save('./shape_input/{0:}.jpg'.format(index))