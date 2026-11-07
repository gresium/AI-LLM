# Iris Flower Classification — Random Forest Model

# Overview
This project builds a machine learning model to classify Iris flower species based on sepal and petal dimensions. The Random Forest algorithm was used for its high accuracy and ability to handle multi-class classification efficiently.

# Objective
Predict the correct Iris species (Setosa, Versicolor, Virginica)
Demonstrate supervised learning with Scikit-learn
Evaluate model accuracy and feature importance

# Dataset
Source: UCI Machine Learning Repository — Iris Dataset
Features:
sepal_length
sepal_width
petal_length
petal_width
Target: species (Setosa, Versicolor, Virginica)
Size: 150 samples, 4 features, 3 classes

# Methodology
Loaded dataset using pandas and scikit-learn
Split data into train/test sets (80/20)
Trained RandomForestClassifier with tuned hyperparameters
Evaluated model using accuracy and confusion matrix
Visualized feature importance

# Results
Accuracy: 97–100% (depending on seed)
Algorithm: RandomForestClassifier
Key Features: Petal length and petal width had the highest importance
The Random Forest model achieved near-perfect accuracy, effectively distinguishing all three Iris species.

# Future Work
Add hyperparameter tuning (GridSearchCV)
Compare with SVM and KNN classifiers
Deploy model via Flask or Streamlit

# Author
Developed by Gresa Hisa (@gresium) — AI & Cybersecurity Engineer
