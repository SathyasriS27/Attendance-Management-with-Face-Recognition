# Facial-Recognition-based-Attendance-Management-System---Codes-and-Idea-behind-it
The main purpose of this project is to build a face recognition-based attendance monitoring system for schools, colleges, and offices to enhance and upgrade the current attendance system into more efficient and effective as compared to before.
This system consists of 4 phases- Dataset creation, face detection, face recognition, attendance. Dataset is made by the pictures of the students in school or college or employees of a workspace. Face detection and recognition are performed by Haar-Cascade classifier and Local Binary Pattern Histogram.
1. Dataset Creation: Images of the students are captured using an external camera. Multiple pictures of a single student are going to be taken with varied gestures and angles. These pictures endure pre-processing. The pictures are cropped to get the Region of Interest (ROI) which will be employed in the recognition method. Then these pictures can be regenerated from RGB to grayscale pictures. These pictures are going to be saved with the student's roll range or identification number.
2. Face Detection: Face detection here is performed with the help of Haar-Cascade Classifier with OpenCV. Haar Cascade algorithmic rule has to be trained to sight human faces before it is used for face detection. This is often referred to as feature extraction. The Haar cascade training knowledge used is the associate XML file- haarcascade_frontalface_default. 
3. Face Recognition: Face recognition method will be divided into 3 steps- prepare the trainer, train face recognizer, prediction. These pictures are the basic unit then used for face recognition. They will be assigned with an integer label of the student it belongs to. These images are then used for face recognition. The face recognizer used in this system is the Local Binary Pattern Histogram. Initially, the list of local binary patterns (LBP) of the entire face is obtained. These LBPs are converted into a decimal number and then histograms of all those decimal values are made. In the end, one histogram will be formed for each image in the training data. Later, during the recognition process histogram of the face to be recognized is calculated and then compared with the already computed histograms and returns the best-matched label associated with the student it belongs to.
4. Attendance: After the face recognition process and after the attendance program is worked on the data got from the face recognition process the recognized faces will be marked as present in the excel sheet and the rest will be marked as absent.

The Software Tools used in this project are:
1. OpenCV
2. Haarcascade Classifier 
3. LBPH
4. PyQt5
5. Pyre base

The order of the codes and their headings:
1. Face Detection 
2. Data Gatherinng 
3. Face Training
4. Face Recognition for a single person using a single camera 
5. Face Recognition for multiple people using a single camera 
6. Attendance Management Program 
7. Face Recognition using two or more cameras 
8. Attendance Mangement Program for Multiple Cameras 
