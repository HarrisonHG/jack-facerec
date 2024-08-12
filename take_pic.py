"""
Takes pictures of the user then converts them to encodings and saves them

press q to quit
and p to take a photo then enter name
"""
import sys
import pickle
import cv2
import face_recognition

CAMINDEX = 0
try:
    cap = cv2.VideoCapture(CAMINDEX)
    ret,frame = cap.read()
    #check if an image can be formed
    if not ret:
        raise ValueError("camera not responding")
except ValueError as error:
    print("Camera is not valid, are you sure its plugged in or in use?")
    sys.exit(1)

#saved as two arrays as the function later requires an array to search through
encodings = []
names = []

while True:
    ret, frame = cap.read()
    cv2.imshow("window",frame)
    #quit if q is pressed
    x = cv2.waitKey(1)

    if x == ord("p"):
        rgbimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(frame)
        encodings.append(face_recognition.face_encodings(rgbimage,boxes))
        names.append(input("input name"))
    elif  x == ord("q"):
        break

cv2.destroyAllWindows()
with open("data.pickle","wb") as f:
    data = {"encodings":encodings,"names":names}
    pickle.dump(data, f)
    f.close()

sys.exit(0)
