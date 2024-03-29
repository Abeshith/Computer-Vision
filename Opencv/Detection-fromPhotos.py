#FACE EYE AND SMILE DETECTION FROM PHOTOS

face_classifier = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('./haarcascade/haarcascade_eye.xml')
smile_classifier = cv2.CascadeClassifier('./haarcascade/haarcascade_smile.xml')


image = cv2.imread("C:/Users/abhes/OneDrive/Pictures/elon-musk.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(gray,1.3,5)

if faces is ():
    print("NO faces")
    
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(10,0,255),2)
    cv2.imshow('face detection',image)
    cv2.waitKey(0)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye_classifier.detectMultiScale(roi_gray)
    smile = smile_classifier.detectMultiScale(roi_gray)
    
    for (ex,ey,ew,eh) in eyes:
           cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(10,0,255),2)
           cv2.imshow('eye detection',image)
           cv2.waitKey(0)
    for (sx,sy,sw,sh) in smile:
         cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(10,0,255),2)
         cv2.imshow('smile detection',image)
         cv2.waitKey(0)
        
        

cv2.destroyAllWindows()