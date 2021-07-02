# Facial Recognition based Attendance Management System

The main purpose of this project is to build a face recognition-based attendance monitoring system for schools, colleges, and offices to enhance and upgrade the current attendance system into more efficient and effective as compared to before.
This system consists of 4 phases- Dataset creation, face detection, face recognition, attendance. Dataset is made by the pictures of the students in school or college or employees of a workspace. Face detection and recognition are performed by Haar-Cascade classifier and Local Binary Pattern Histogram.

1. **Dataset Creation:** Images of the students are captured using an external camera. Multiple pictures of a single student are going to be taken with varied gestures and angles. These pictures endure pre-processing. The pictures are cropped to get the Region of Interest (ROI) which will be employed in the recognition method. Then these pictures can be regenerated from RGB to grayscale pictures. These pictures are going to be saved with the student's roll range or identification number.
2. **Face Detection:** Images of the students are captured using an external camera. Multiple pictures of a single student are going to be taken with varied gestures and angles. These pictures endure pre-processing. The pictures are cropped to get the Region of Interest (ROI) which will be employed in the recognition method. Then these pictures can be regenerated from RGB to grayscale pictures. These pictures are going to be saved with the student's roll range or identification number.
3. **Face Recognition:** Face recognition method will be divided into 3 steps- prepare the trainer, train face recognizer, prediction. These pictures are the basic unit then used for face recognition. They will be assigned with an integer label of the student it belongs to. These images are then used for face recognition. The face recognizer used in this system is the Local Binary Pattern Histogram. Initially, the list of local binary patterns (LBP) of the entire face is obtained. These LBPs are converted into a decimal number and then histograms of all those decimal values are made. In the end, one histogram will be formed for each image in the training data. Later, during the recognition process histogram of the face to be recognized is calculated and then compared with the already computed histograms and returns the best-matched label associated with the student it belongs to.
4. **Attendance:** After the face recognition process and after the attendance program is worked on the data got from the face recognition process the recognized faces will be marked as present in the excel sheet and the rest will be marked as absent.

## Software Tools Used

1. OpenCV
2. Haarcascade Classifier 
3. LBPH
4. PyQt5
5. Pyrebase

## Order of the codebase and their file names

1. Camera Check
2. Face Detection 
3. Data Gatherinng 
4. Face Training
5. Face Recognition for a single person using a single camera - [`Recognition.py`](https://github.com/SathyasriS27/Facial-Recognition-based-Attendance-Management-System---Codes-and-Idea-behind-it/blob/main/5-Recognition.py)
6. Face Recognition for multiple people using a single camera - [`multipleRecognition.py`](https://github.com/SathyasriS27/Facial-Recognition-based-Attendance-Management-System---Codes-and-Idea-behind-it/blob/main/6-multiplerecog.py)
7. Attendance Management Program - [`PresentorAbsent.py`](https://github.com/SathyasriS27/Facial-Recognition-based-Attendance-Management-System---Codes-and-Idea-behind-it/blob/main/7-Presentorabsent.py)
8. Attendance Mangement Program for Multiple Cameras - [`PresentorAbsentformultiple.py`](https://github.com/SathyasriS27/Facial-Recognition-based-Attendance-Management-System---Codes-and-Idea-behind-it/blob/main/8-PresentorAbsentformultiple.py)
9. Face Recognition using Multiple cameras - [`Multiplecameras.py`](https://github.com/SathyasriS27/Facial-Recognition-based-Attendance-Management-System---Codes-and-Idea-behind-it/blob/main/10-multiplecameras.py)
 
