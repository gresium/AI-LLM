#  Face Recognition System

# Description
Implemented a Face Recognition System using Python and OpenCV to detect, encode, and recognize faces from images or real-time video streams.
The project demonstrates data preprocessing, feature extraction, and real-time face matching with accuracy evaluation.

# Objectives
Detect and recognize human faces using OpenCV.
Encode and compare facial features.
Perform real-time recognition via webcam.
Evaluate recognition accuracy and reliability.

# Methodology
Face Detection – Used OpenCV’s Haar Cascade or face_recognition library for identifying faces in frames.
Feature Extraction – Encoded facial features into numerical vectors.
Model Training – Stored face encodings and labels for known individuals.
Recognition & Matching – Compared new faces against stored encodings.
Performance Evaluation – Calculated recognition accuracy and response time.
Tech Stack
Python 3.x
OpenCV
NumPy
face_recognition (dlib-based)
# Usage
Clone and run the notebook:
git clone https://github.com/<your-username>/Face-Recognition-Project.git

cd Face-Recognition-Project

jupyter notebook "Face Recognition Project.ipynb"

# Output
Real-time webcam face recognition.
Bounding boxes and labels for identified faces.
Accuracy metrics and visual performance summary.

# Results
The system successfully detects and recognizes multiple faces in real time with high accuracy and minimal latency.

# Author
Developed by Gresa Hisa  — AI & Cybersecurity Engineer
