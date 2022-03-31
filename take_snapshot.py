import cv2
import time
import random

def take_snapshot():
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)

    result = True

    while (result):
        #read the frames while the camera is on
        ret, frame = videoCaptureObject.read()

        #cv2.imwrite() function is used to save an image to any storage device
        cv2.imwrite("NewPicture1.jpg",frame)
        result = False

    #Turns the camera off / to close the camera
    videoCaptureObject.release()

    #closes all the windows that might be opened while this process
    cv2.destroyAllWindows()

take_snapshot()