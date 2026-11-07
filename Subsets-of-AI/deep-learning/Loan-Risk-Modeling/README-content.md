# Loan Default Prediction — Lending Club Dataset Overview
This project predicts whether a borrower will default on a loan using Lending Club historical data. The dataset was imbalanced, so class balancing, encoding, and model evaluation techniques were applied to ensure accurate and fair predictions.

# Objective
Predict loan default probability
Handle class imbalance with SMOTE
Evaluate using Recall, Precision, and ROC-AUC

# Dataset
Source: Lending Club loan data (loan_data.csv)
Target column: not.fully.paid
0 → Loan repaid
1 → Loan defaulted
Class balance: 84% repaid, 16% defaulted

# Methodology
Loaded and inspected dataset using pandas
Checked for missing values (none found)
Visualized imbalance and applied SMOTE
Encoded categorical variables via OneHotEncoder
Split data into 80/20 train/test sets
Trained a Scikit-learn MLPClassifier
Evaluated metrics: Recall, Precision, ROC-AUC
Optimized decision threshold using Youden’s J statistic

# Results
ROC AUC: 0.805
Recall (Sensitivity): 0.697
Precision: 0.738
Best Threshold (Youden J): 0.4777
Train/Test Split: 80/20 (Train: 12,872 | Test: 3,218)
The neural network model demonstrated strong discrimination between repaid and defaulted loans. SMOTE effectively balanced the dataset.

# Future Work
Hyperparameter tuning (hidden layers, max_iter)
Feature selection and scaling improvements
Benchmark against Random Forest or XGBoost

# Author
Developed by Gresa Hisa (@gresium) — AI & Cybersecurity Engineer
