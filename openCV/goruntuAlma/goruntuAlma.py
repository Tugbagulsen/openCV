import cv2
import numpy as np

#0, bağlı olan ilk kamerayı temsil eder. Eğer birden fazla kamera varsa, 1, 2, 3, ... şeklinde sıralanır.
#2 deediğimizde videodaki görüntüyü açar
kamera = cv2.VideoCapture(0)

#ret kameranın çalışıp çalışmadığını kontrol etmek amacıyla oluşturuldu
#görüntü gelen görüntüyü ard arda ekler ve bu sayede video çıkar
while True:
    ret,goruntu = kamera.read()
    
    cv2.imshow("tg", goruntu)
    #q basana kadar döngü devam eder 30 ms de bir görüntü ekler
    if cv2.waitKey(30) & 0xFF == ("q"):
        break
    
kamera.release()

cv2.destroyAllWindows()
