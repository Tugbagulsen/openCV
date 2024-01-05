import cv2
import numpy as np

resim = cv2.imread("C:/Users/tugba/Desktop/openCV/belliKismaEfektYapma/kudus.jpg")
#r = 2 g = 1 b = 0 sırayla bu kısıma ne girersen resmin üzerine o renk eklenir
#[:,:,:]1. parametre y 2. parametre x yani yukarıdan aşağıya soldan sağa 3. parametre bgr
resim[150:200,150:350,0] = 0
resim[150:200,150:350,1] = 0
resim[150:200,150:350,2] = 255

cv2.imshow("Kudüs", resim)

cv2.waitKey(0)
cv2.destroyAllWindows