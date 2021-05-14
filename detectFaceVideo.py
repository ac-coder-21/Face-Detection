import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

videoCapture = cv2.VideoCapture(0)

while True:
    _, img = videoCapture.read()


    grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faceCoordinates = face_cascade.detectMultiScale(grayScale, 1.1, 4)

    for (x, y, w, h) in faceCoordinates:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

videoCapture.release()