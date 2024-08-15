'''
Holds all functions for the code
'''
import sys
import cv2
import logging

# Log level should be set in the main script
logger = logging.getLogger(__name__)

def camera_connection(camindex = 0):
    '''
    handles all connections to the camera and errors 
    camindex is the index of the camera as according to the OS
    returns a cv2 videocapture device
    '''
    try:
        cap = cv2.VideoCapture(camindex)
        ret= cap.read()[0]
        #check if an image can be formed
        if not ret:
            raise ValueError("camera not responding")
        
        # If we reach this point the camera has connected successfully
        logger.debug("Camera connected at index: " + str(camindex))
    except ValueError:
        logger.warning("Camera is not valid, are you sure its plugged in or in use?")
        sys.exit(1)
    return cap

if __name__ == "__main__":
    print("This module is not intended to be run directly. Please see main.py")
    sys.exit(1)

def removevalue(array,value = "Unknown"):
	for i in array:
		if i == value:
			array.remove(i)
	return array
