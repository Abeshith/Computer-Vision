# Detection of FullBody of Human From vidoes
import cv2
body_capture = cv2.CascadeClassifier('./haarcascade/haarcascade_fullbody.xml')
video = cv2.VideoCapture('./walking.avi')

while video.isOpened():
     ret, frame = video.read()
     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     body = body_capture.detectMultiScale(gray,1.2,5)
     
     for (x,y,w,h) in body:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(20,0,255),2)
            cv2.imshow('video',frame)
    
     if cv2.waitKey(1) == 13:
            break
            
video.release()
cv2.destroyAllWindows()
