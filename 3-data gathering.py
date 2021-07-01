#for data gathering - making the dataset 
import cv2
from decimal import Decimal 

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
face_detector = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

# Inputting the data into the csv file - used as the main register to store the students names and roll no.
with open('RegisterDetails.csv','r+') as f:
    myDatalist = f.readlines()
    namelist=[]
    for line in myDatalist:
        entry=line.split(',')
        namelist.append(entry[0])
        Name=input("enter the students name")
        Rollno=Decimal(input("enter the roll no."))
        if Rollno not in namelist:
            f.writelines(f'\n{Rollno},{Name}') 
            break
#printing the given informmation for final confirmation 
print("student name is ",Name)
print("Roll No. is",Rollno)
print("\n [INFO] Initializing face capture. Look the camera and wait ...")

# Initialize individual sampling face count
count = 0
while(True):
    ret, img = cam.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(Rollno) + '.' +  
                    str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()