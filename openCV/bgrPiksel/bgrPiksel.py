import cv2
import numpy as np

kurtResmi = cv2.imread("C:/Users/tugba/Desktop/openCV/bgrPiksel/kurt.jpg")

cv2.imshow("Kurt Resmi", kurtResmi)

#230 aşağı 80 sağa pikselin bgr değerini yazdırır
print(kurtResmi[(230,80)])

#Resmin boyutunu yazdırıcak +str yazmamın sebebi stringin yanına 
#sonuç yazdıracak olması 
print("Resmin Boyutu: " +str(kurtResmi.size))
print("Resmin Özellikleri: "+str(kurtResmi.shape))
print("Resmin veri tipi: "+str(kurtResmi.dtype))

cv2.waitKey(0)
cv2.destroyAllWindows()