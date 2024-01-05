import cv2
import numpy as np

hrm = cv2.imread("C:/Users/tugba/Desktop/openCV/resimdeBolgeselKareAlma/hrm.jpg")

#Belli bir bölgeyi kare içerisine alma fonksiyonu
#ilk parametre hangi resmi kullanacaksın
#ikinci parametre sol alt köşeyi belirt
#üçüncü parametre sağ üst köşe çaprazlama
cv2.rectangle(hrm, (400,130), (250,320),[0,0,255], 3)
#hrm[50:100,230:310,0]=255

cv2.imshow("HarryRonHermonie", hrm)
cv2.waitKey(0)
cv2.destroyAllWindows()