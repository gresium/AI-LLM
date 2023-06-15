# Diabetes Prediction using K-Nearest Neighbors (KNN)

# Description
Built and evaluated a K-Nearest Neighbors (KNN) model to predict diabetes using patient health data.
Includes preprocessing, model training, accuracy evaluation, and visualizations showing how different k values affect prediction performance 

# Repository Structure
Diabities KNN -> Main Notebook
README.md -> Project Documentation

# Dataset
Dataset derived from the Pima Indians Diabetes Database (UCI Repository).
Features:
Pregnancies
Glucose
BloodPressure
SkinThickness
Insulin
BMI
DiabetesPedigreeFunction
Age
Outcome (0 = No diabetes, 1 = Diabetes)

# Methodology
Data Preprocessing
Handle missing or invalid values.
Normalize numeric features.
Model Training
Apply KNN classifier with various k values.
Split data into training and test sets.

# Evaluation
Compute accuracy, precision, recall, and F1-score.
Generate confusion matrix for visual clarity.
Visualization
Plot accuracy vs. k.
Show confusion matrix and key metrics.

# Dependencies
Install required packages:
pip install numpy pandas matplotlib seaborn scikit-learn
Usage

# Clone the repository and open the notebook:
git clone https://github.com/<your-username>/Diabetes-KNN-Model.git

cd Diabetes-KNN-Model

# jupyter notebook "Diabities KNN Model.ipynb"
Output
Model accuracy and confusion matrix.
Visualization of performance across k values.
Insights into diabetes prediction trends.
Results
The model achieved approximately 75–80% accuracy using an optimal k value range between 5–10, demonstrating strong performance for this dataset.

# Author
Gresa Hisa
AI Engineer & Cybersecurity Engineer
