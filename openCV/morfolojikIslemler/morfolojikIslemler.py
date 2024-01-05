import cv2
import numpy as np
#resim eklemeye üşendim

#Morfoloji Nedir?
#Biçim veya yapı anlamına gelir 
#Amaç ise bir yapılandırma elemanı kullanarak nesnelerin yapısını 
#veya biçimini dönüştürmektir.

image = cv2.imread(" ")
#Yapılandırma elemanı:
kernel = np.ones((5,5),np.unit8)
#Genişleme işlemleri yapyor nesnenin kalınlığını ve boyutun arttırıyor
#dilation = cv2.dilate(image,kernel, iterations=1)
#Daraltma işlemi yapıyor dilationun tam aksini, gürültülerden arınmış bir görüntü oluyor.
erosion = cv2.erode(image, kernel, iterations=1)

cv2.imshow("Orjinal", image)
#cv2.imshow("Dilation", dilation)
cv2.imshow("Erosion", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()

#önce erosion işlemi sonra dilation işlemi yapılır, 
#önce görüntü gürültüden arındırılır sonra resmin üzerinde oynanır Yaniiii:

import cv2
import numpy as np

image = cv2.imread(" ")
#Yapılandırma elemanı:
kernel = np.ones((5,5),np.unit8)

erosion = cv2.erode(image, kernel, iterations=1)
dilation = cv2.dilate(erosion,kernel, iterations=1)

cv2.imshow("Orjinal", image)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()

#iteraations 1 değilde 2 olurs yaptığı işlemi daha güçlü yapar
