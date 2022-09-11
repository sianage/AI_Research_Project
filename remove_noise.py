import PIL
from random import  randint
from PIL import Image
import os
from scipy import ndimage, misc
import numpy as np
#import cv2
img = Image.open(f"C:\\Users\\siana\\Desktop\\backup\\{image}")
pixels = img.load()
width = img.size[0]
height = img.size[1]
'''rand1 = randint(0, 255)
rand2 = randint(rand1, 255)
noise = randint(rand1, rand2)'''
noise = randint(0,255)
for x in range(width):
    for y in range(height):
        r = pixels[x,y][0]
        g = pixels[x,y][1]
        b = pixels[x,y][2]
        if (r and g and b) < noise//2:
            pixels[x,y] = (randint(0,noise),randint(0,noise),randint(0,noise))
        elif ((r and g)<noise//2) and (b > (255 - noise//2)):
                pixels[x,y] = (randint(0,noise),randint(0,noise), randint((b - noise // 2),(b + noise // 2)))
        elif ((r and b) < (noise // 2)) and (g > (255 - noise // 2)):
                pixels[x, y] = (randint(0, noise), randint((g - noise // 2), (g + noise // 2)), randint(0, noise))
        elif (((g and b) < noise // 2) and (r > (255 - noise // 2))):
                pixels[x, y] = (randint((r - noise // 2), (r + noise // 2)), randint(0, noise), randint(0, noise))
        elif (r < noise // 2) and (g and b) > 255 - noise // 2:
                pixels[x, y] = (randint(0, noise), randint((g - noise // 2), (g + noise // 2)),
                randint((b - noise // 2), (b + noise // 2)))
        elif (g < noise // 2) and (r and b) > 255 - noise // 2:
                pixels[x, y] = (randint((r - noise // 2), (r + noise // 2)), randint(0,noise),
                randint((b - noise // 2), (b + noise // 2)))
        elif (b < noise // 2) and (r and g) > 255 - noise // 2:
                pixels[x,y] = (randint((r - noise // 2), (r + noise // 2)),randint((g - noise // 2), (g + noise // 2)),
                randint(0,noise))
        else:
            pixels[x,y] = (randint((b - noise // 2), (b + noise // 2)),
            randint((g - noise // 2), (g + noise // 2)),
            randint((b - noise // 2), (b + noise // 2)))
img.save(f"C:\\Users\\siana\\Desktop\\adversary\\{image}")