"""
detect faces and draw a box around them
"""
import sys
import pickle
import cv2
import face_recognition
CAMINDEX = 0
font = cv2.FONT_HERSHEY_SIMPLEX
FONTSCALE = 1
textcolor = (255, 0, 0)
#get webcam
cap = cv2.VideoCapture(CAMINDEX)
with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

Knownencodings = data["encodings"]
names = data["names"]

while True:
    q , frame = cap.read()
    boxes = face_recognition.face_locations(frame)
    encodings = face_recognition.face_encodings(frame, boxes)
    matches = []
    for e,encoding in enumerate(encodings):
        matches = face_recognition.compare_faces(Knownencodings,encoding)
        print(matches)
        print(e)

    for e,i in enumerate(matches):
        if i:
            print("BOXES",boxes)
            top,right,bottom,left = boxes[0]
            cv2.rectangle(frame, (left,top), (right,bottom) , (0,255,0), 4)
            image = cv2.putText(frame, names[e], (left-20,top-20), font, FONTSCALE,
            textcolor, 1, cv2.LINE_AA, False)

    cv2.imshow("window",frame)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
sys.exit()
