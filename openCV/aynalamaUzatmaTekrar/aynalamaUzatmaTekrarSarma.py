import cv2
import numpy as np

asker = cv2.imread("C:/Users/tugba/Desktop/openCV/aynalamaUzatmaTekrar/asker.jpg")
cv2.imshow("Asker", asker)
#Resmin aynalanmasını istiyorsam o resmi yeni değişkenin içerisine atmam gerek
#Sınır yapıcağımı ve kopyalayacağımı söylüyorum copyBorder 
# ilk parametre hangi değişkene sınırlama yapacağın
#4 parametre ekleyeceksin sağ sol üst alt
#cv2.BORDER_REFLECT aynalama işlemi için kullanılır
aynalananResim = cv2.copyMakeBorder(asker,150,150,200,200,cv2.BORDER_REFLECT)
cv2.imshow("Aynalanan",aynalananResim)

uzatilanResim = cv2.copyMakeBorder(asker, 175,175,175,175,cv2.BORDER_REPLICATE)
cv2.imshow("Uzatilan",uzatilanResim)

tekrarResim = cv2.copyMakeBorder(asker, 100,100,100,100, cv2.BORDER_WRAP)
cv2.imshow("Tekrarlanan", tekrarResim)

sarilanResim = cv2.copyMakeBorder(asker, 150,150,150,150, cv2.BORDER_CONSTANT, value = (0,0,255))
cv2.imshow("Sarilan", sarilanResim)


cv2.waitKey(0)
cv2.destroyAllWindows()