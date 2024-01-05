import cv2
import numpy as np

hermione = cv2.imread("C:/Users/tugba/Desktop/openCV/resmiGrilestirme/hg.jpg")

#Resmi grileştirme fonksiyonu
#İkisi arasındaki fark?
#Gri kanalını kullanırsaam 3 kanaldan tek kanala düşürmüş oluruz boyut olarak renkli grini 3 katı oluyor
#Hesaplama ve Bellek Verimliliği elde ederiz
hermioneGri = cv2.cvtColor(hermione, cv2.COLOR_BGR2GRAY)

yukseklik, genislik, kanalSayisi = hermione.shape
print("Orjinal", yukseklik,genislik,kanalSayisi)

yukseklik,genislik = hermioneGri.shape
print("Gri Resim", yukseklik,genislik)

cv2.imshow("Orjinal", hermione)
cv2.imshow("Gri", hermioneGri)
#-------------------------------#
#Basit Grileştirme#
hermione2 = cv2.imread("C:/Users/tugba/Desktop/openCV/resmiGrilestirme/hg.jpg", 0)
cv2.imshow("Basit", hermione2)


cv2.waitKey(0)
cv2.destroyAllWindows()