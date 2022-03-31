import dropbox
import cv2
import random
import time

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)

    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)

    result = True
    
    while(result):
        ret, frame = videoCaptureObject.read()

        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)

        start_time = time.time
        result = False

    return img_name
    print("Snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "LUw2pIBJaIYAAAAAAAAAAdXVXt9X_AuB9dujPUwD0yWmfyrxdT4EASJ7zbBRvHYQ"

    file = img_name
    file_from = file
    file_to = "/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.Writemode.overwrite)

        print("The file has been uploaded")

def main():
    while(True):
        if(time.time()-start_time >= 5):
            name = take_snapshot()
            upload_file(name)

main()