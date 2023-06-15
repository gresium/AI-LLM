# Employee Turnover Analysis
Predict employee attrition and surface drivers of churn using EDA and supervised learning.

# Goals
Quantify key churn factors
Train baseline and ensemble models to predict left_company
Explain predictions with feature importance and SHAP
Provide actionable thresholds for HR intervention
Dataset
Target: left_company (0 = stayed, 1 = left)
Features: tenure, age, job_role, department, salary_band, performance_score, overtime, commute_time, satisfaction, engagement, last_promotion_years, manager_changes, training_hours, etc.
Source: HRIS export or synthetic sample

# Methods
Preprocessing: missing handling, outlier caps, encoding, scaling, stratified split, SMOTE or class weights
Models: Logistic Regression, Random Forest, XGBoost (or LightGBM)
Evaluation: ROC-AUC, PR-AUC, F1, Recall, confusion matrix
Interpretation: permutation importance, SHAP global and local explanations, partial dependence

# Repository Contents
Employee Turnover Analysis.ipynb — main notebook
data/ — raw and processed datasets
models/ — trained model artifacts
reports/figures/ — plots and SHAP visuals
reports/metrics/ — evaluation results
README.md — documentation

# QuickStart
Create a virtual environment
python -m venv .venv
Activate it
macOS/Linux: source .venv/bin/activate
Windows: .venv\Scripts\activate
Install dependencies
pip install -U pip wheel
pip install numpy pandas scikit-learn xgboost shap matplotlib plotly seaborn imbalanced-learn pyarrow
Launch the notebook
jupyter lab or jupyter notebook
Notebook Workflow
Config and imports
Data loading and audit
Exploratory analysis
Feature engineering
Data preprocessing and split
Model training
Evaluation and threshold tuning
SHAP interpretation and feature importance
Export model and reports
Metrics to Report
ROC-AUC and PR-AUC
F1, Precision, Recall, Specificity
Recall@k or Precision@k
Turnover cost impact
Ethical Use
Audit bias across demographics
Exclude protected attributes
Human review required for all automated outputs

# Author
Developed by Gresa Hisa (@gresium) — AI & Cybersecurity Engineer
