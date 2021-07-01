import urllib.request
import cv2
import numpy as np
import pandas as pd
from datetime import date
from datetime import datetime
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

#haarcasacade classsifer being used and the trainer being called 
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

# internal camera 
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
#connecting to external camera 
url='http://192.168.1.7:8080/shot.jpg'#change the url according to the one on the device

# Define min window size to be recognized as a face
minW = 0.1*cap.get(3)
minH = 0.1*cap.get(4)  

# Detect the coordinates
detector = dlib.get_frontal_face_detector()

#connecting to the extrenal camera for data input and web cam - as two cameras at a time 
while True:
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, frame = cap.read()
    frame = cv2.flip(frame,1) 
    gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_external=detector(gray)
    faces1 = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(70,70)
    )
    faces_internal=detector(gray1)
    faces11 = faceCascade.detectMultiScale(
        gray1,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize = (int(minW), int(minH)),
    )
    name_external=[]
    id_external=[]
    name_internal=[]
    id_internal=[]
    # Iterator to count faces
    #for external camera 
    i1 = 0
    for face in faces_external:
        # Get the coordinates of faces
        x, y = face.left(), face.top()#gives the left and the top point from the detector 
        x1, y1 = face.right(), face.bottom()#gives the right and the bottom point from the detector
    #to print the rectangle on the face 
    for (x,y,x1,y1) in faces1:
        cv2.rectangle(img,(x,y),(x+x1,y+y1),(255,0,0),2)
        id1, confidence1 = recognizer.predict(gray[y:y+y1,x:x+x1])
        # If confidence is less them 100 ==> "0" : perfect match 
        if (confidence1 < 100):
            Check1 = pd.read_csv("RegisterDetails.csv")
            Name_List=Check1.Name
            N=len(Name_List)
            j=0
            while(j<=N):
                if(j==id1):
                    Name=Name_List[j]
                    name_external.append(Name)
                    id_external.append(id1)
                    break
                j=j+1
            i11=Name
            confidence1 = "  {0}%".format(round(100-confidence1))   
        else:
            i11= "unknown"
            confidence1 = "  {0}%".format(round(100-confidence1))
        cv2.putText(
                    img, 
                    str(i11), 
                    (x+5,y-5), 
                    font, 
                    2, 
                    (255,255,255), 
                    2
                   )
        cv2.putText(
                    img, 
                    str(confidence1), 
                    (x+5,y+y1-5), 
                    font, 
                    2, 
                    (255,255,0), 
                    2
                   )
        # Increment iterator for each face in faces
        i1 = i1+1 
    # Iterator to count faces
    #for internal camera 
    i2 = 0
    for face1 in faces_internal:
        # Get the coordinates of faces
        x11, y11 = face1.left(), face1.top()#gives the left and the top point from the detector 
        x111, y111 = face1.right(), face1.bottom()#gives the right and the bottom point from the detector
    #to print the rectangle on the face 
    for (x11,y11,x111,y111) in faces11:
        cv2.rectangle(frame,(x11,y11),(x11+x111,y11+y111),(255,0,0),2)
        id1, confidence = recognizer.predict(gray1[y11:y11+y111,x11:x11+x111])
        # If confidence is less them 100 ==> "0" : perfect match 
        if (confidence < 100):
            Check1 = pd.read_csv("RegisterDetails.csv")
            Name_List=Check1.Name
            N=len(Name_List)
            j=0
            while(j<=N):
                if(j==id1):
                    Name=Name_List[j]
                    name_internal.append(Name)
                    id_internal.append(id1)
                    break
                j=j+1
            i22=Name
            confidence = "  {0}%".format(round(100-confidence))   
        else:
            i22= "unknown"
            confidence = "  {0}%".format(round(100-confidence))
        cv2.putText(
                    frame, 
                    str(i22), 
                    (x11+5,y11-5), 
                    font, 
                    2, 
                    (255,255,255), 
                    2
                   )
        cv2.putText(
                    frame, 
                    str(confidence), 
                    (x11+5,y11+y111-5), 
                    font, 
                    2, 
                    (255,255,0), 
                    2
                   )
        # Increment iterator for each face in faces
        i2 = i2+1 
    print("the total number of faces seen on the external camera right now is ",i1)
    print("the total number of faces seen on the internal camera right now is ",i2) 
    width = 640
    height = 380
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    #showing the resized image 
    cv2.imshow("Resized image", resized)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cv2.waitKey(30)
cv2.destroyAllWindows()

#printing the names and corresponding ids - for checking ; to see the names that are going to be transferred to the datforattendance.csv 
print("People seen on the external camera \t",name_external,"\n People seen on the internal camera \t",name_internal)
print("People's Id seen on the external camera \t",id_external,"\n People's Id seen on the internal camera \t",id_internal)
Id_total=[]
Id_total=id_external+id_internal #joins both the lists 
print(Id_total)#for a confirmation on the joining of two lists 
#in order to remove the repeated ids from the list
res = []
for i in Id_total:
    if i not in res:
        res.append(i)
# printing list after removal 
print ("The Ids after removing duplicates : " + str(res))
#now getting the names from the ids 
#using register details Csv
Check4 = pd.read_csv("RegisterDetails.csv")
Name22=Check4.Name
Id22=Check4.No
N1=len(Name22)
fin_name=[]
fin_id=[]
N2=len(res)
b=0
while(b<N2):
    m=0
    while(m<N1):
        if(res[b]==Id22[m]):
            fin_name.append(Name22[m])  
            fin_id.append(Id22[m]) 
        m=m+1
    b=b+1
print("final name list",fin_name)
print("final id list ",fin_id)
N3=len(fin_name)
#calling the attendance function to write the data into the dataforattendance csv 
#loop for entery of data in the excel sheet 
#calling the function 
k=0
while (k<N3):
    markattendance(fin_name[k],fin_id[k])
    k=k+1

