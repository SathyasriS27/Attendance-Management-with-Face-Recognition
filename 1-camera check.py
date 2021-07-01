#camera check 
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width of the dialog box 
cap.set(4,480) # set Height of the dialog box 
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)#colour image is shown
    cv2.imshow('gray', gray)#grayscale image is shown 
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()