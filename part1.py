from PIL import Image
import numpy as np
import cv2
import math

width=946
height=481
img = Image.open("test.png")
newimg = Image.new("RGB", (width, height), "white")
for x in range(1, width-1): 
    for y in range(1, height-1):

        
        Gx = 0
        Gy = 0

        
        p = img.getpixel((x-1, y-1))
        r = p[0]
        g = p[1]
        b = p[2]

        
        intensity = r + g + b

       
        Gx += -intensity
        Gy += -intensity

        
        p = img.getpixel((x-1, y))
        r = p[0]
        g = p[1]
        b = p[2]

        Gx += -2 * (r + g + b)

        p = img.getpixel((x-1, y+1))
        r = p[0]
        g = p[1]
        b = p[2]

        Gx += -(r + g + b)
        Gy += (r + g + b)

        
        p = img.getpixel((x, y-1))
        r = p[0]
        g = p[1]
        b = p[2]

        Gy += -2 * (r + g + b)

        p = img.getpixel((x, y+1))
        r = p[0]
        g = p[1]
        b = p[2]

        Gy += 2 * (r + g + b)

        
        p = img.getpixel((x+1, y-1))
        r = p[0]
        g = p[1]
        b = p[2]

        Gx += (r + g + b)
        Gy += -(r + g + b)

        p = img.getpixel((x+1, y))
        r = p[0]
        g = p[1]
        b = p[2]

        Gx += 2 * (r + g + b)

        p = img.getpixel((x+1, y+1))
        r = p[0]
        g = p[1]
        b = p[2]

        Gx += (r + g + b)
        Gy += (r + g + b)

       
        length = math.sqrt((Gx * Gx) + (Gy * Gy))

        
        length = length / 4328 * 255

        length = int(length)

        
        newimg.putpixel((x,y),(length,length,length))
cv2.imshow("image", np.float32(newimg))
cv2.imwrite("part1.png",np.float32(newimg))
cv2.waitKey(0)