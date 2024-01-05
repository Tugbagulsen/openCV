

#Filtreleme nedir?
#Görüntüde istenmeyen özellikleri kaldırır
#Farklı filtreleme tekniklerinin gürültüyü gidermede veya 
#görüntünün belli yerlerinde belirginleştirme gibi kendine özel işlevleri vardır
#Gürültüyü giderme nedir?
#Bir görüntü üzerindeki istenmeyen ve rastgele piksel değerlerini veya dalgalanmaları azaltmayı veya kaldırmayı ifade eder. 
#Gürültü, bir görüntünün gerçek dünya koşullarında çekilmesi, 
#işlenmesi veya iletilmesi sırasında eklenen istenmeyen veya rastgele özelliklerdir.
#Meanin Filtering (ortalama filtreleme): bir görüntü üzerinde gürültüyü azaltmak veya pürüzsüzleştirmek amacıyla kullanılan bir filtreleme tekniğidir. 
#3-3 şablonda 9 pikselin ortalmasını ortanca piksele yazar 
#Bu filtreleme yöntemi, bir pikselin değerini ve çevresindeki piksellerin değerlerini kullanarak yeni bir değer oluşturur.
#Bir pencere seçilir
#Pencere içindeki değerler alınır
#Ortalama hesaplanır
#Yeni değer atanır

import cv2
import numpy as np

image = cv2.imread("")

meanFilter = cv2.blur(image(3,3))
meanFilter2 = cv2.blur(image(5,5))
meanFilter3 = cv2.blur(image(7,7))

cv2.imshow("Orjinal resim", image)
cv2.imshow("Mean Filter", meanFilter)
cv2.imshow("Mean Filter2", meanFilter2)
cv2.imshow("Mean Filter3", meanFilter3)

cv2.waitKey(0)
cv2.destroyAllWindows()


#Medyan filtreleme, bir pikselin değerini çevresindeki piksellerin medyan değeri ile değiştirerek çalışır. 
#Medyan, bir sayı dizisinin sıralanmış hali içinde ortadaki değeri ifade eder.Medyan filtreleme, 
#bir pikselin değerini çevresindeki piksellerin medyan değeri ile değiştirerek çalışır. 
#Medyan, bir sayı dizisinin sıralanmış hali içinde ortadaki değeri ifade eder.Medyan filtreleme, 
#bir pikselin değerini çevresindeki piksellerin medyan değeri ile değiştirerek çalışır. 
#Medyan, bir sayı dizisinin sıralanmış hali içinde ortadaki değeri ifade eder.Medyan filtreleme, 
#bir pikselin değerini çevresindeki piksellerin medyan değeri ile değiştirerek çalışır. 
#Medyan, bir sayı dizisinin sıralanmış hali içinde ortadaki değeri ifade eder.
#Belirli bir pencere (kernel) seçilir. Bu pencere genellikle 3x3, 5x5, 7x7 gibi tek sayı boyutlarına sahip kare bir matris olabilir.
#Seçilen pencere içindeki piksellerin değerleri sıralanır.
#Sıralanmış değerlerin ortasındaki değer (medyan), orijinal pikselin yeni değeri olarak atanır.

import cv2
import numpy as np

image = cv2.imread("")

meanFilter = cv2.blur(image(3,3))
meanFilter2 = cv2.blur(image(5,5))
meanFilter3 = cv2.blur(image(7,7))

medianFilter = cv2.medianBlur(image, 3)
medianFilter2 = cv2.medianBlur(image, 5)
medianFilter3 = cv2.medianBlur(image, 7)

gauss = cv2.GaussianBlur(image(3,3),0)
gauss = cv2.GaussianBlur(image(5,5),0)
gauss = cv2.GaussianBlur(image(7,7),0)

cv2.imshow("Orjinal resim", image)

cv2.imshow("Mean Filter", meanFilter)
cv2.imshow("Mean Filter2", meanFilter2)
cv2.imshow("Mean Filter3", meanFilter3)

cv2.imshow("Median Filter", medianFilter)
cv2.imshow("Median Filter", medianFilter2)
cv2.imshow("Median Filter", medianFilter3)

cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.GaussianBlur fonksiyonundaki 0 (sıfır) parametresi, Gaussian çekirdeğinin standart sapmasını belirtir. 
#Standart sapma, Gauss fonksiyonunun yayılma veya "genişlik" derecesini kontrol eder. 
#fonksiyonundaki 0 (sıfır) parametresi, Gaussian çekirdeğinin standart sapmasını belirtir. 
#Standart sapma, Gauss fonksiyonunun yayılma veya "genişlik" derecesini kontrol eder.