import cv2
import numpy as np

hp1 = cv2.imread("C:/Users/tugba/Desktop/openCV/agirlikliToplama2/hp1.jpg")
hp2 = cv2.imread("C:/Users/tugba/Desktop/openCV/agirlikliToplama2/hp2.jpg")

cv2.imshow("HP1", hp1)
cv2.imshow("HP2", hp2)

#Resimleri üst üste toplama fonksiyonu add

toplam = cv2.add(hp1, hp2)
cv2.imshow("Toplam", toplam)
agirlikliToplama = cv2.addWeighted(hp1,)

cv2.waitKey(0)
cv2.destroyAllWindows()