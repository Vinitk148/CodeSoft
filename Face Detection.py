import cv2

face_cap = cv2.CascadeClassifier("D:\\apps\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)

while True:
    open, data = video.read()
    if not open:
        break
    col = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
    faces = face_cap.detectMultiScale(
        col, scaleFactor=1.1, minNeighbors=5, minSize=(50,50), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(data, (x, y), (x+w, y+h), (0,100,0), 1)

    cv2.imshow("camera", data)
    if cv2.waitKey(20) == ord("q"):
        break
video.release()