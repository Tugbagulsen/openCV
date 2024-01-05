import cv2
import numpy as np
#adaptive tresholding
#gri tonlamalı olmalıdır
image = cv2.imread("C:/Users/tugba/Desktop/openCV/esikAyarlama/asker.jpg", 0)

#simple tresholding
ret,thresh1=cv2.threshold(image,160,255, cv2.THRESH_BINARY)

#adaptive tresholding
tresh2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
    cv2.THRESH_BINARY,11,2)
tresh3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
    cv2.THRESH_BINARY,11,2)

cv2.imshow("Orjinal", image)
cv2.imshow("thres1", thresh1)
cv2.imshow("thres2", tresh2)
cv2.imshow("thres3", tresh3)

cv2.waitKey(0)
cv2.destroyAllWindows()