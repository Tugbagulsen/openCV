import cv2
import numpy as np

image = cv2.imread("C:/Users/tugba/Desktop/openCV/kenarAlgilama/resim1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)

#görüntülerdeki piksel yoğnluklarını hesaplama
def autoCanny(blur, sigma = 0.33):
    median = np.median(blur)
    lower = int(max(0,(1.0-sigma)*median))
    upper = int(min(255,(1.0+sigma)*median))
    canny = cv2.Canny(blur, lower, upper)
    
    return canny

wide = cv2.Canny(blur, 10,220)
tight = cv2.Canny(blur,200,230)
auto = autoCanny(blur)



cv2.imshow("orjinal image", image)
cv2.imshow("edges", np.hstack([wide,tight,auto]))

#canny = cv2.Canny(blur, 50,150)
#cv2.imshow("canny image", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()