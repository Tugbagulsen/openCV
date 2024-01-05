import cv2
import numpy as np

#Bir matris döndürüyor aslında birden fazla liste elemanı tutan yapı tutuyor 
#Bir parametre olarak boyutlarını ve kaç kanaldan oluşmasını istediğimizi yazıyoruz
#İkinci parametrede ise saklayacağımız değerin ne olduğunu soruyor
#Yani parametre olarak shape ile dataType soruyor

resim = np.zeros((300,300,3),dtype=np.uint8)

print(resim)

cv2.waitKey(0)
cv2.destroyAllWindows()