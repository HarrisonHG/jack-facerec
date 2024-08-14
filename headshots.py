import logging
import cv2
import os

# Logging levels affect many dependencies as well as current script.
# Change the verbosity of logs by changing the level to one of the following:
# CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
# Whatever level is set, that level and all levels more severe it will be logged.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATASET_FOLDER = "dataset"
NAME = 'donkeykong' #replace with your name

cam = cv2.VideoCapture(0)

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)

if not os.path_exists(DATASET_FOLDER):
    logger.debug("Creating dataset folder at " + DATASET_FOLDER)
    os.makedirs(DATASET_FOLDER)
if not os.path_exists(NAME):
    logger.debug("Creating new folder for " + NAME)
    os.makedirs(NAME)

img_counter = 0

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
    elif k%256 == 32:
        # SPACE pressed
        img_name = DATASET_FOLDER + "/"+ NAME +"/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        logger.info("{} written!".format(img_name))
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
