# Import required libraries
import cv2
import numpy as np
from datetime import date
from datetime import datetime
import pandas as pd 
import dlib

#importing the data into an excel sheet for attendance-for multiple students at a time 
def markattendance(Name,ID):
    with open('Dataforattendance.csv','r+') as f:
        myDatalist = f.readlines()
        namelist=[]
        for line in myDatalist:
            entry=line.split(',')
            namelist.append(entry[0])
            current_date = date.today()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            timestring=current_time
            pt = datetime.strptime(timestring,'%H:%M:%S')
            total_seconds = pt.second + pt.minute*60 + pt.hour*3600
        f.writelines(f'\n{ID},{Name},{current_date},{now},{total_seconds}')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

# Connects to your computer's default camera
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height  
  
# Detect the coordinates
detector = dlib.get_frontal_face_detector()

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)  
  
# Capture frames continuously
while True:
    # Capture frame-by-frame
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    # RGB to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=detector(gray)
    faces1 = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    name=[]
    id=[]
    # Iterator to count faces
    i = 0
    for face in faces:
        # Get the coordinates of faces
        x, y = face.left(), face.top()#gives the left and the top point from the detector 
        x1, y1 = face.right(), face.bottom()#gives the right and the bottom point from the detector
    for(x,y,x1,y1) in faces1:
        cv2.rectangle(frame, (x,y), (x+x1,y+y1), (0,255,0), 2)
        id1, confi = recognizer.predict(gray[y:y+y1,x:x+x1])
        confi=int(confi)
        # If confidence is less them 100 ==> "0" : perfect match 
        if (int(confi) < int(100)):
            Check1 = pd.read_csv("RegisterDetails.csv")
            Name_List=Check1.Name
            N=len(Name_List)
            j=0
            while(j<=N):
                if(j==id1):
                    Name=Name_List[j]
                    name.append(Name)
                    id.append(id1)
                    break
                j=j+1
            i1=Name
            confi = "  {0}%".format(round(100-confi))   
        else:
            i1= "unknown"
            confi = "  {0}%".format(round(100-confi))
        cv2.putText(
                    frame, 
                    str(i1), 
                    (x+5,y-5), 
                    font, 
                    1, 
                    (255,255,255), 
                    2
                   )
        cv2.putText(
                    frame, 
                    str(confi), 
                    (x+5,y+y1-5), 
                    font, 
                    1, 
                    (255,255,0), 
                    1
                   )  
        # Increment iterator for each face in faces
        i = i+1
    #total number of faces seen on camera are 
    print("the total number of faces seen on camera right now is ",i) 
    # Display the resulting frame
    cv2.imshow('frame', frame)
  
    # This command let's us quit with the "esc" button on a keyboard.
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Release the capture and destroy the windows
cam.release()
cv2.destroyAllWindows()

#printing the names and corresponding ids - for checking ; to see the names that are going to be transferred to the datforattendance.csv 
print(name)
print(id)
print(i)

#loop for entery of data in the excel sheet 
#calling the function 
k=0
while (k<i):
    markattendance(name[k],id[k])
    k=k+1
    
    




