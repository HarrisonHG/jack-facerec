"""
detect faces and draw a box around them
"""
import sys
import cv2
import face_recognition
import functions
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CAMINDEX = 0

cap = functions.camera_connection(CAMINDEX)

logger.debug("Begin face detection...")
while True:
    q , frame = cap.read()

    face_count = len(face_recognition.face_locations(frame))
    if (face_count > 0):
        logger.Debug("Faces detected: " + str(face_count))
        
    for top,right,bottom,left in face_recognition.face_locations(frame):
        cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0), 5)

    cv2.imshow("window",frame)
    if cv2.waitKey(1) == ord("q"):
        break

logger.debug("Q pressed. Exiting...")
cv2.destroyAllWindows()
sys.exit()
