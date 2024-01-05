import cv2
import numpy as np

soloTr = cv2.imread("C:/Users/tugba/Desktop/openCV/goruntuPramidi/soloTr.jpeg")

#Orjinal Resmi iki kat büyütür
ikiKat = cv2.pyrUp(soloTr)

#Orjinal boyutu 2 kat küçültür
ikiKatKucuk = cv2.pyrDown(soloTr)

print("SoloTr", soloTr.shape)
print("SoloTrx2", ikiKat.shape)
print("SoloTr-x2", ikiKatKucuk.shape)

cv2.imshow("SoloTr", soloTr)
cv2.imshow("SoloTrx2", ikiKat)
cv2.imshow("SoloTr-x2", ikiKatKucuk)

cv2.waitKey(0)
cv2.destroyAllWindows()