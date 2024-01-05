import numpy as np 
import cv2

#Görüntüyü okuma, çeşitli dosya formatlarındaki görüntüleri okuyabilir 
#ve bellekte bir Numpy dizisi olarak temsil eder.
resim = cv2.imread("bir.png", 0)

#Resim çıktığı zaman pencerede sol tarafta resimle ilgili bir şeyler yazar
cv2.imshow("Teknofest Hatirasi", resim)
#Bir görüntüyü belirli bir dosya yoluna kaydetmek için kullanılan bir fonksiyondur
#Okunan resmi yeni bir dosyaya kaydet
cv2.imwrite("yeniresim.png", resim)
#Herhangi bir tuşa bastığımızda bekler, pencere açıldığında herhangi bir tuşa bastığımızda pencere kapanmaz bekler
cv2.waitKey(0)

#Çarpıya bastığımızda openCV bağlı tüm pencerelerin kapanmasını söylerim, hafızadanda siler.
cv2.destroyAllWindows()
