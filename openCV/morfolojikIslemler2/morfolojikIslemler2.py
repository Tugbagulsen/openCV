import cv2
import numpy as np
#resim eklemey üşendim
image = cv2.imread(" ")
#Yapılandırma elemanı:
kernel = np.ones((5,5),np.unit8)

erosion = cv2.erode(image, kernel, iterations=1)
dilation = cv2.dilate(erosion,kernel, iterations=1)

#opening işlemi erosion ve dilation işlemiyle anlı işlemleri yapar
#Opening estirme daha kolay

opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#kopuk kısımlar tamamlar gürültü gidermez
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

#dilationdan erosion çıkarılıyor ortaya gradyan çıkıyor çok saçma ama anlatımı bu 
gradyan = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

#resmi kaldırıp sadece grültüyü gösterior ön planı kaldırır ve arka planı gösterir
tophat = cv2.morphologyEx(image,cv2.MORPH_TOPHAT, kernel)

#Closing ve orjinal resim araındaki farkı çıkartıyor
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Orjinal", image)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
cv2.imshow("Gradyan", gradyan)
cv2.imshow("Tophat", tophat)
cv2.imshow("Blackhat", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()