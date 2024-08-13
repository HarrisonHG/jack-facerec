'''
Holds all functions for the code
'''
import sys
import cv2

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
    except ValueError:
        print("Camera is not valid, are you sure its plugged in or in use?")
        sys.exit(1)
    return cap

if __name__ == "__main__":
    print("This module is not intended to be run directly. Please see main.py")
    sys.exit(1)
