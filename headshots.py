'''
This code takes pictures of the user its recommended to take multiple per person
'''
import os
import logging
import cv2
import functions

# Logging levels affect many dependencies as well as current script.
# Change the verbosity of logs by changing the level to one of the following:
# CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
# Whatever level is set, that level and all levels more severe it will be logged.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATASET_FOLDER = "dataset"
CAMINDEX = 0
WINDOW_WIDTH=500
WINDOW_HEIGHT=300

cam = functions.camera_connection(CAMINDEX)
name = input("your name") #replace with your name

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", WINDOW_WIDTH, WINDOW_HEIGHT)

if not os.path.exists(DATASET_FOLDER):
    logger.debug("Creating dataset folder at %s", DATASET_FOLDER)
    os.makedirs(DATASET_FOLDER)
if not os.path.exists(name):
    logger.debug("Creating new folder for %s", name)
    os.makedirs(DATASET_FOLDER +"/"+ name)
img_counter = 0# pylint: disable=invalid-name

while True:
    ret, frame = cam.read()
    if not ret:
        logger.error("Failed to grab frame. Please check camera connection.")
        break
    cv2.imshow("press space to take a photo", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        logger.info("Escape hit, closing...")
        break
    if k%256 == 32:
        # SPACE pressed
        img_name = f"{DATASET_FOLDER}/{name}/image_{img_counter}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} written!")
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
