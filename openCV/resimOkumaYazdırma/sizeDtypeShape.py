import cv2
import numpy as np

resim1 = cv2.imread("akinci.png")
resim2 = cv2.imread("bir.png")

cv2.imshow("Akinci", resim1)

#Resmin boyutunun ne kadar olduğunu öğrenmek istersek
print(resim1.size) #Boyutu
print(resim1.dtype) #Hangi tipte veri kullandığı öğrenilir
print(resim1.shape) #Genişliği, yüksekliği, kaç kanaldan oluştuğunu gösterir

cv2.waitKey(0)
cv2.destroyAllWindows()
