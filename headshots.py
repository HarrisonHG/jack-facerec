import cv2
import os
import functions

DATASET_FOLDER = "dataset"
NAME = 'donkeykong' #replace with your name
CAMINDEX = 0

cam = functions.camera_connection(CAMINDEX)

if not os.path.exists(DATASET_FOLDER):
    os.makedirs(DATASET_FOLDER)
    
if not os.path.exists(DATASET_FOLDER+"/"+NAME):
    os.makedirs(DATASET_FOLDER +"/"+ NAME)

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)



img_counter = 0

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
    elif k%256 == 32:
        # SPACE pressed
        img_name = DATASET_FOLDER+"/"+ NAME +"/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cv2.destroyAllWindows()
