import urllib.request
import cv2
import numpy as np


cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width of the dialog box 
cap.set(4,480) # set Height of the dialog box 
# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.1.7:8080/shot.jpg'#change the url according to the one on the device 
while True:
    # Use urllib to get the image and convert into a cv2 usable format
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # put the image on screen
    print('Original Dimensions : ',img.shape)
    width = 640
    height = 480
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    print('Resized Dimensions : ',resized.shape)
    cv2.imshow("Resized image", resized)
    cv2.imshow('frame', frame)
    #To give the processor some less stress
    #time.sleep(0.1) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
