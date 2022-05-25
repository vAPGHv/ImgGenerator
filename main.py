from PIL import Image, ImageDraw
import random
from colorit import background as bg
from os import system

system("clear")  #clear linux terminal
system("cls")  #clear windows terminal

rint = "random.randint(0, 255)"

color = "(eval(rint), eval(rint), eval(rint))"

rsize = "random.randint(1, 200)"

x = eval(rsize)
y = eval(rsize)

size = (x,y)
name = "img.png"

img = Image.new("RGBA", size)

img.save(name)

colsr = 0
colsrl = []

colsg = 0
colsgl = []

colsb = 0
colsbl = []

with Image.open(name) as img:
    
    dimg = ImageDraw.Draw(img)
    
    for y in range(img.size[0]):
        for x in range(img.size[1]):
            
            pix = (x, y)
            
            col = eval(color)
            
            dimg.line(pix+pix, col)
            
            print(bg(f"Pixel - x: {pix[0]}, y: {pix[1]}\nColor: {col}", (col[0], col[1], col[2])), end="")  # print pixel and color
            print("\n")
            
            colsr += col[0]
            colsg += col[1]
            colsb += col[2]
            
            colsrl.append(col[0])
            colsgl.append(col[1])
            colsbl.append(col[2])
    
    img.save(name)

print(f"x: {x}")
print(f"y: {y}\n")

red = round(colsr / len(colsrl))
green = round(colsg / len(colsgl))
blue = round(colsb / len(colsbl))

print(bg(f"red: {red}", (red, 0, 0)))  # print red
print(bg(f"green: {green}", (0, green, 0)))  # print green
print(bg(f"blue: {blue}", (0, 0, blue)))  # print blue

print(bg("  ", (red, green, blue)))
