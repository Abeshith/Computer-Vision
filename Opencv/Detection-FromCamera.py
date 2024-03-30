## FACE EYE AND SMILE DETECTION FROM CAMERA
import cv2
face_classifier = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('./haarcascade/haarcascade_eye.xml')
smile_classifier = cv2.CascadeClassifier('./haarcascade/haarcascade_smile.xml')

def detect(gray,frame):
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(10,0,255),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]
         eyes = eye_classifier.detectMultiScale(roi_gray,1.1,3)
         for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(125,50,255),2)
    return frame

video_capture = cv2.VideoCapture(0)
while True:
    _,frame = video_capture.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas = detect(gray,frame)
    cv2.imshow('Video',canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
