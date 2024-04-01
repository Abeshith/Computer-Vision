import cv2
import time
car_classifier = cv2.CascadeClassifier('./haarcascade/haarcascade_car.xml')
video = cv2.VideoCapture('./image_examples_cars.avi')

while video.isOpened():
    time.sleep(.02)
    ret , frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    car = car_classifier.detectMultiScale(gray,1.2,5)
    
    for (x,y,w,h) in car:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow('cars_video',frame)
        
    if cv2.waitKey(1) == ord('q'):
        break
        
video.release()
cv2.destroyAllWindows()
