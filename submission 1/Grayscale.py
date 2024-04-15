import cv2
import numpy as np
from numpy import random

img = cv2.imread('./computer_vision_midterm_2024_3455136-main/Resources/sun_moon_lake.png')
img = cv2.resize(img, (480, 360), interpolation=cv2.INTER_AREA)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); #to gray

for y in range(0,len(img_gray)):
    for x in range(0,len(img_gray[y])):
        if img[y][x][0]==150 and img[y][x][1]==100 and img[y][x][2]==10:  
            img_gray[y][x]=100


cv2.imshow('dot', img_gray)
cv2.waitKey(0) 
cv2.destroyAllWindows()