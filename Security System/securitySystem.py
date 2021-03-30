import cv2
from cv2 import cv2

import time
import random
import dropbox


startTime=time.time()

def takeSnapshots():
    videoCaptureObject=cv2.VideoCapture(0)
    result=True

    while(result):
        #Read is a method used to read the frames while the camera is on
        ret,frame=videoCaptureObject.read()

        imageName="image"+str(random.randint(0,100))+".png"
        #imwrite is a method used to save the snaps
        cv2.imwrite(imageName,frame)
        startTime=time.time()

        result=False

    videoCaptureObject.release()
    cv2.destroyAllWindows()
    print("Snapshot taken")
    return(imageName)

def uploadFile(imageName):
    accessToken=""
    fileFrom=imageName
    fileTo="/imagesFolder/"+imageName
    dbx=dropbox.Dropbox(accessToken)
    f=open(fileFrom,'rb')
    dbx.files_upload(f.read(),fileTo)
    print("File Uploaded")


def main():
    while(True):
        #time.gmtime(0)-which day will time.time() starts calculating
        if(time.time()-startTime>=5):
            name=takeSnapshots()
            uploadFile(name)

main()


