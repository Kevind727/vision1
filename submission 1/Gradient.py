import cv2
import numpy as np
from numpy import random

img = cv2.imread('./computer_vision_midterm_2024_3455136-main/Resources/sun_moon_lake.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); #to gray

max=0
ax=0
ay=0
for y in range(0,len(img_gray)-32,32):
    for x in range(0,len(img_gray[y])-32,32):
        block=img_gray[y:y+32,x:x+32]   
        summ=sum(sum(block))
        if summ>max:           
            ax=x
            ay=y
            print(ax,ay)
            max=summ

print(ax)
print(ay)
img_gray=cv2.rectangle(img_gray, (ax,ay), (ax+32,ay+32), (0,255,255), 2)

cv2.imshow('dot', img_gray)
cv2.waitKey(0) 
cv2.destroyAllWindows()