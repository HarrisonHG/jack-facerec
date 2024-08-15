#! /usr/bin/python

# import the necessary packages
import sys
from imutils import paths
import face_recognition
import pickle
import cv2
import os
def train_model(window_name,progress_callback,frame, window_width):
    '''
    Takes the photos in the folders and uses them to train the model for later recognition.
    takes a callback for a progress bar progress callback must expect the following variables 
    progress_callback(frame,length,togo,loaded = 0,y = 0,thickness = 20) 
    window_name - the name of the window to display on
    frame - the frame that it will draw on
    length - the total length it should span
    togo - the total number of jobs to complete
    loaded - the number of these jobs done
    y - the y at which it starts at (the uppermost part of the bar)
    thickness- how far the bar should go downwards
    '''
    SAVE_FILE = "encodings.pickle"
    # our images are located in the dataset folder
    imagePaths = list(paths.list_images("dataset"))
    if not os.path.exists(SAVE_FILE):
        data = {"encodings":[],"names":[]}
        logger.info("No encoding file exists running face detection only")
    else:
        with open(SAVE_FILE, "rb") as f:
            data = pickle.load(f)
    # initialize the list of known encodings and known names
    knownEncodings = data["encodings"]
    knownNames = data["names"]
    
    # loop over the image paths
    for (i, imagePath) in enumerate(imagePaths):
        # extract the person name from the image path
        
        frame = progress_callback(window_name,frame,window_width,len(imagePaths),i + 1)
        #print(window_name,frame,window_width,len(imagePaths),i + 1)
        name = imagePath.split(os.path.sep)[-2]

        # load the input image and convert it from RGB (OpenCV ordering)
        # to dlib ordering (RGB)
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # detect the (x, y)-coordinates of the bounding boxes
        # corresponding to each face in the input image
        boxes = face_recognition.face_locations(rgb,
            model="hog")

        # compute the facial embedding for the face
        encodings = face_recognition.face_encodings(rgb, boxes)

        # loop over the encodings
        for encoding in encodings:
            # add each encoding + name to our set of known names and
            # encodings
            knownEncodings.append(encoding)
            knownNames.append(name)
    # dump the facial encodings + names to disk
    data = {"encodings": knownEncodings, "names": knownNames}
    f = open("encodings.pickle", "wb")
    f.write(pickle.dumps(data))
    f.close()
    return frame

if __name__ == "__main__":
    print("This module is not intended to be run directly. Please see main_withdc.py")
    sys.exit(1)
