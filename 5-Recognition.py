import cv2
from datetime import date
from datetime import datetime
import pandas as pd 
from decimal import Decimal

#defining a function which would help in transferring the name , id , time of entry and exit into an excel sheet 
def markattendance(Name):
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
        f.writelines(f'\n{id},{Name},{current_date},{now},{total_seconds}')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
while True:
    ret, img =cam.read()
    img = cv2.flip(img, 1) 
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # If confidence is less them 100 ==> "0" : perfect match 
        if (confidence < 100):
            Check1 = pd.read_csv("RegisterDetails.csv")
            Name_List=Check1.Name
            N=len(Name_List)
            i=0
            while(i<=N):
                if(i==id):
                    Name=Name_List[i]
                    break
                i=i+1
            i1=Name
            confidence = "  {0}%".format(round(100-confidence))   
        else:
            i1= "unknown"
            confidence = "  {0}%".format(round(100-confidence))
        cv2.putText(
                    img, 
                    str(i1), 
                    (x+5,y-5), 
                    font, 
                    1, 
                    (255,255,255), 
                    2
                   )
        cv2.putText(
                    img, 
                    str(confidence), 
                    (x+5,y+h-5), 
                    font, 
                    1, 
                    (255,255,0), 
                    1
                   )  
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()

#Transfering the data into an excel sheet for attendance 
markattendance(Name)




