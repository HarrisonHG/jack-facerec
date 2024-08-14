'''
This code takes pictures of the user its recommended to take multiple per person
'''
import os
import cv2
import functions

DATASET_FOLDER = "dataset"
name = input("your name") #replace with your name
CAMINDEX = 0
WINDOW_WIDTH=500
WINDOW_HEIGHT=300
cam = functions.camera_connection(CAMINDEX)

if not os.path.exists(DATASET_FOLDER):
    os.makedirs(DATASET_FOLDER)

if not os.path.exists(DATASET_FOLDER+"/"+NAME):
    os.makedirs(DATASET_FOLDER +"/"+ NAME)

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", WINDOW_WIDTH, WINDOW_HEIGHT)



img_counter = 0# pylint: disable=invalid-name

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("press space to take a photo", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    if k%256 == 32:
        # SPACE pressed
        img_name = f"{DATASET_FOLDER}/{NAME}/image_{img_counter}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} written!")
        img_counter += 1

cv2.destroyAllWindows()
