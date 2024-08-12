"""
detect faces and draw a box around them
"""
import sys
import cv2
import face_recognition
import functions

cap = functions.camera_connection()

while True:
    q , frame = cap.read()
    #detect the faces
    for top,right,bottom,left in face_recognition.face_locations(frame):
        cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0), 5)

    cv2.imshow("window",frame)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
sys.exit()
