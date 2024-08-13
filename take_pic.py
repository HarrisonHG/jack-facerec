"""
Takes pictures of the user then converts them to encodings and saves them

press q to quit
and p to take a photo then enter name
"""
import sys
import pickle
import cv2
import face_recognition
import functions
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CAMINDEX = 0

cap = functions.camera_connection(CAMINDEX)

#saved as two arrays as the function later requires an array to search through
encodings = []
names = []

logger.info("Ready for encoding. Press p to take a picture and q to quit.")
while True:
    ret, frame = cap.read()
    cv2.imshow("window",frame)
    x = cv2.waitKey(1)

    if x == ord("p"):
        rgbimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(frame)
        encodings.append(face_recognition.face_encodings(rgbimage,boxes))
        names.append(input("input name"))
    elif  x == ord("q"):
        break

logger.debug("Exit button pressed. Pickling the images...")
with open("data.pickle","wb") as f:
    data = {"encodings":encodings,"names":names}
    pickle.dump(data, f)
    f.close()
    logger.debug("Images pickled successfully to: " + f.name)

logger.debug("Exiting...")
cv2.destroyAllWindows()
sys.exit(0)
