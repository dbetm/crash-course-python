import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('atardecer.jpeg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.xlabel("Valor de intensidad")
plt.ylabel("Número de píxeles")
plt.tight_layout()
plt.show()
