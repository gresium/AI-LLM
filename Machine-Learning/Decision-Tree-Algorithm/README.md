# Diamonds Price Prediction – Decision Tree Regression

## Overview
This project builds a **Decision Tree Regression model** to predict diamond prices based on key physical and quality attributes. It demonstrates supervised machine learning on structured tabular data, focusing on feature relationships, model interpretability, and regression performance.

## Objective
- Predict diamond prices using measurable features  
- Understand how attributes like **carat, cut, color, and clarity** influence price  
- Train and evaluate a Decision Tree regression model  
- Visualize decision logic and feature importance  

## Dataset
- **Source:** Diamonds dataset  
- **Target variable:** `price`  
- **Features:**  
  - carat  
  - cut  
  - color  
  - clarity  
  - depth  
  - table  
  - x, y, z (dimensions)

## Methodology
1. Data loading and inspection  
2. Handling categorical features via encoding  
3. Feature selection and preprocessing  
4. Train/test split  
5. Model training using **DecisionTreeRegressor**  
6. Model evaluation and visualization  

## Model
- **Algorithm:** Decision Tree Regression  
- **Learning Type:** Supervised Machine Learning  
- **Framework:** scikit-learn  

## Evaluation
- R² score  
- Mean Squared Error (MSE)  
- Comparison of predicted vs. actual prices  
- Feature importance analysis  

## Key Insights
- **Carat** is the strongest driver of diamond price  
- Quality attributes (cut, color, clarity) significantly impact valuation  
- Decision Trees provide clear interpretability but may overfit without tuning  

## Tech Stack
- Python  
- Pandas, NumPy  
- scikit-learn  
- Matplotlib, Seaborn  
- Jupyter Notebook  

## Future Work
- Hyperparameter tuning (`max_depth`, `min_samples_split`)  
- Compare with Random Forest and Gradient Boosting  
- Add cross-validation for robustness  

## Author
Developed by **Gresa Hisa (@gresium)**  
AI & Machine Learning Engineer | Cybersecurity Engineer



