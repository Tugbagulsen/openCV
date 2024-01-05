import cv2
import numpy as np

resim = np.zeros((300,300,3),dtype=np.uint8)

#Çizgi oluşturma
#pt1 = nereden başlasın
#pt2 = nereye kadar gitsin
#color = rengi ne olsun
#kalınlığı ne olsun
cv2.line(resim, (0,0), (100,100), (0,0,255), 3)

#Daire oluşturma
#Dairenin merkezi
#Dairenin yarı çapı
#renk
cv2.circle(resim,(150,150),25,(25,0,255),3)

#Metin kutusu oluşturma
#Metin ekle
#Başlangıç piksel belirt
#Yazı tipi ekle
#Yazı boyutu
#Renk belirt
#Kalınlık
cv2.putText(resim, "tg", (200,200), cv2.FONT_HERSHEY_COMPLEX, 2,(255,0,0), 3)


cv2.imshow("deneme line", resim)

cv2.waitKey(0)
cv2.destroyAllWindows