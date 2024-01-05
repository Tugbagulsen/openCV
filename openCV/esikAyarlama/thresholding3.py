import cv2
import numpy as np
#otsu tresholding
#gri tonlamalı olmalıdır
image = cv2.imread("C:/Users/tugba/Desktop/openCV/esikAyarlama/asker.jpg", 0)

#simple tresholding
ret,thresh1=cv2.threshold(image,160,255, cv2.THRESH_BINARY)

#otsu tresholding
ret2, tresh2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("Orjinal", image)
cv2.imshow("thres1", thresh1)
cv2.imshow("thres2", tresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()