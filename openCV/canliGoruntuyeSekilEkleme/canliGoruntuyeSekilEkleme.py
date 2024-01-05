import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret,goruntu = kamera.read()
    #diktördgen ekleme
    #Başlangıç noktasını belirle
    #nereye kadar süreceğini belirle
    #color belirle
    #kalınlık
    cv2.rectangle(goruntu, (100,100),(200,200),(25,36,55),2)
    cv2.line(goruntu,(0,0),(100,100),(255,150,15),4)
    cv2.circle(goruntu, (150,150),50,(80,150,35),1)
    cv2.putText(goruntu, "Tugba",(220,220),cv2.FONT_HERSHEY_DUPLEX,1,(200,0,0),1)
    cv2.imshow("TG", goruntu)
    
    if cv2.waitKey(25) & 0xFF == ('q'):
        break
    
kamera.release()
cv2.destroyAllWindows()