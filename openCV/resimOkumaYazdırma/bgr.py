import cv2
import numpy as np

#Resimdeki her bir piksel 8 bitten oluşur
#max(1,1,1,1,1,1,1,1)
#129+64+32+16+8+4+2+1 = 255 bir bitin en fazla alabileceği değer 255 
#min(0,0,0,0,0,0,0,0) = 0 bir bitin en az alabileceği değer 0

resim = cv2.imread("akinci.png")

cv2.imshow("Akinci", resim)
#Ben resimde kaç piksel olduğunu öğrenmek için matrissel karşılığını görmek için
print(resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
