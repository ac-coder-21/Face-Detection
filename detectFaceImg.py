import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('image.jpg')

grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faceCo = face_cascade.detectMultiScale(grayScale, 1.1, 4)

for (x, y, w, h) in faceCo:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()