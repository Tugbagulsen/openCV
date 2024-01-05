import cv2
import numpy as np

resim1 = ()
resim2 = ()

bit_And = cv2.bitwise_and(resim1,resim2)
bit_not = cv2.bitwise_not(resim1,resim2)
bit_or = cv2.bitwise_or(resim1,resim2)
bit_xor = cv2.bitwise_xor(resim1,resim2)

cv2.imshow("ilk resim",resim1)
cv2.imshow("ilk resim",resim2)
cv2.imshow("and", bit_And)
cv2.imshow("not", bit_not)
cv2.imshow("or", bit_or)
cv2.imshow("xor", bit_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()