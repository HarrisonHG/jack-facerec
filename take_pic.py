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
#get webcam
cap = cv2.VideoCapture(CAMINDEX)
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
with open("encodings.pickle","wb") as f:
    pickle.dump(encodings, f)
    f.close()
with open("names.pickle","wb") as f:
    pickle.dump(names, f)
    f.close()
sys.exit()
