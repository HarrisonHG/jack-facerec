"""
detect faces and draw a box around them
"""
import sys
import time
import logging
import pickle
import cv2
import face_recognition
import functions

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CAMINDEX = 0
SAVE_FILE = "encodings.pickle"
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONTSCALE = 1
TEXTCOLOUR = (255, 0, 0)

with open(SAVE_FILE, "rb") as f:
    data = pickle.load(f)
known_encodings = data["encodings"]
names = data["names"]

cap = functions.camera_connection(CAMINDEX)

logger.debug("Begin face detection...")
while True:
    q , frame = cap.read()
    boxes = face_recognition.face_locations(frame)
    encodings = face_recognition.face_encodings(frame, boxes)
    face_count = len(encodings)
    if face_count > 0:
        logger.Debug("Faces detected: " + str(face_count))
    else:
        # No face detected, so save some CPU cycles
        time.sleep(0.01)

    matches = []
    for e,encoding in enumerate(encodings):
        matches = face_recognition.compare_faces(known_encodings,encoding)

        print(matches)
        print(e)

    for e,i in enumerate(matches):
        if i:
            print("BOXES",boxes)
            top,right,bottom,left = boxes[0]
            cv2.rectangle(frame, (left,top), (right,bottom) , (0,255,0), 4)
            image = cv2.putText(frame, names[e], (left-20,top-20), FONT, FONTSCALE,
            TEXTCOLOUR, 1, cv2.LINE_AA, False)

    cv2.imshow("window",frame)
    if cv2.waitKey(1) == ord("q"):
        break

logger.debug("Q pressed. Exiting...")
cv2.destroyAllWindows()
sys.exit()
