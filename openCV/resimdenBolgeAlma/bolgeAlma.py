import cv2
import numpy as np

prens = cv2.imread("C:/Users/tugba/Desktop/openCV/resimdenBolgeAlma/prens.jpg")
#50'den 150 piskele kadar yukarıdan aşağı, 300'den 400 piksele kadar soldan sağa
kesit = prens[50:150, 300:400]
#kesilen alanı seçilen alana ekleme yani üst ısımda kesilen alanı aldık aşağıda 
#hizasını ayarladığımız kısıma yapıştırdı
prens[0:100, 0:100] = kesit
#resime efekt eklemek istersem bunu yaparız
prens[ :, :, 0] = 255
#spesifik bir alanı boyamak istersem
prens[400:450, 300:350] = (0,150,255)
cv2.imshow("Prens" , prens)
cv2.waitKey(0)
cv2.destroyAllWindows()