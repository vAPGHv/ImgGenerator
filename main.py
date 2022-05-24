from PIL import Image, ImageDraw
import random

rint = ("random.randint(0, 255)")

color = "(eval(rint), eval(rint), eval(rint))"

size = (50, 50)
name = "img.png"

img = Image.new("RGBA", size)

img.save(name)

with Image.open(name) as img:
    
    dimg = ImageDraw.Draw(img)
    
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            
            pix = (x, y)
            
            dimg.line(pix+pix, eval(color))
    
    img.save(name)
