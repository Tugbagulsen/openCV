import cv2
import numpy as np

tsk1 = cv2.imread("C:/Users/tugba/Desktop/openCV/agirlikToplama/tsk1.jpg")
tsk2 = cv2.imread("C:/Users/tugba/Desktop/openCV/agirlikToplama/tsk2.jpeg")

print(tsk1[100,200])
print(tsk2[300,430])

cv2.imshow("Tsk1", tsk1)
cv2.imshow("Tsk2", tsk2)

print(tsk1[100,200]+tsk2[300,430])

cv2.waitKey(0)
cv2.destroyAllWindows()

#bgr değerlerinde min 0 max 255 değer alır. 
#Toplama işlemi yapılırken 255'i geçen değerde sıfırdan başlanır
#250+10=260 ancak 260 olarak bir bgr değeri yoktu bu yüzden 260-255=5 yani bgr değeri 5