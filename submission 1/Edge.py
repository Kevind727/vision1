import cv2
import numpy as np
from numpy import random

img = cv2.imread('./computer_vision_midterm_2024_3455136-main/Resources/sun_moon_lake.png')
img = cv2.resize(img, (480, 360), interpolation=cv2.INTER_AREA)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); #to gray
Horizontal = cv2.Sobel(img_gray, -1, 0, 1, 3, 3)  #sobel Horizontal
veritcal = cv2.Sobel(img_gray, -1, 1, 0, 3, 3)  #sobel veritcal

cv2.imshow('Horizontal', Horizontal)
cv2.imshow('veritcal', veritcal)
cv2.waitKey(0) 
cv2.destroyAllWindows()