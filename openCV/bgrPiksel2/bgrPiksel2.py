import cv2
import numpy as np

resim = cv2.imread("C:/Users/tugba/Desktop/openCV/bgrPiksel2/hp.jpg")

#Soldan 50 piksel aşağı 30 piksel sağa verilen değerde boya
resim[50,30] = [255,255,255]

#Belirli bir alan kadar boyama
for i in range(100):
    resim[70,i] = [255,255,255]

cv2.imshow("resim", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()