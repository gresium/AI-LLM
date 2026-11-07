# Twitter Hate Speech Classification (Logistic Regression + TF-IDF)

## Overview
This project builds a text classification model to detect **hate speech** in tweets (`label = 1`) vs **non-hate** tweets (`label = 0`).  
It includes tweet-specific preprocessing, TF-IDF vectorization, Logistic Regression training, class-imbalance handling, and hyperparameter tuning with stratified cross-validation.

---

## Dataset
**Columns**
- `id`: tweet identifier
- `label`: `0` = non-hate, `1` = hate
- `tweet`: raw tweet text

---

## Workflow

### 1) Text Preprocessing (Tweet Cleanup)
Steps applied to each tweet:
- Normalize casing (lowercase)
- Remove user handles (e.g., `@user`)
- Remove URLs (e.g., `http...`, `www...`)
- Remove `#` symbol while keeping the hashtag word
- Tokenize using `TweetTokenizer` (NLTK)
- Remove stopwords
- Remove redundant tokens (`rt`, `amp`, etc.)
- Remove tokens with length `1`

Output: each tweet becomes a cleaned list of tokens, then tokens are joined back into a string for vectorization.

---

### 2) Feature Engineering (TF-IDF)
- Used `TfidfVectorizer(max_features=5000)`
- `fit_transform()` on training set
- `transform()` on test set (prevents data leakage)

---

### 3) Model Training (Logistic Regression)
Models trained:
1. **Baseline Logistic Regression** (default parameters)
2. **Balanced Logistic Regression** using `class_weight="balanced"` to address class imbalance
3. **Tuned Logistic Regression** using `GridSearchCV` + `StratifiedKFold` optimizing **recall**

---

### 4) Model Evaluation
Metrics reported:
- **Accuracy**
- **Recall** (for class `1` hate)
- **F1-score** (for class `1` hate)

---

## Results (Example)
> Replace with your actual notebook output if different.

**Best GridSearch Parameters**
- `C`: `1`
- `penalty`: `l2`
- `class_weight`: `balanced`
- `cv`: `StratifiedKFold(n_splits=4)`
- `scoring`: `recall`

**Test Set Performance (Best Estimator)**
- Recall (hate=1): ~0.77
- F1 (hate=1): ~0.58

---

## How to Run

### Requirements
```bash
pip install pandas numpy scikit-learn nltk

# Twitter Hate Speech Classification (Logistic Regression + TF-IDF)

## Overview
This project builds a text classification model to detect **hate speech** in tweets (`label = 1`) vs **non-hate** tweets (`label = 0`).  
It includes tweet-specific preprocessing, TF-IDF vectorization, Logistic Regression training, class-imbalance handling, and hyperparameter tuning with stratified cross-validation.

---

## Dataset
**Columns**
- `id`: tweet identifier
- `label`: `0` = non-hate, `1` = hate
- `tweet`: raw tweet text

---

## Workflow

### 1) Text Preprocessing (Tweet Cleanup)
Steps applied to each tweet:
- Normalize casing (lowercase)
- Remove user handles (e.g., `@user`)
- Remove URLs (e.g., `http...`, `www...`)
- Remove `#` symbol while keeping the hashtag word
- Tokenize using `TweetTokenizer` (NLTK)
- Remove stopwords
- Remove redundant tokens (`rt`, `amp`, etc.)
- Remove tokens with length `1`

Output: each tweet becomes a cleaned list of tokens, then tokens are joined back into a string for vectorization.

---

### 2) Feature Engineering (TF-IDF)
- Used `TfidfVectorizer(max_features=5000)`
- `fit_transform()` on training set
- `transform()` on test set (prevents data leakage)

---

### 3) Model Training (Logistic Regression)
Models trained:
1. **Baseline Logistic Regression** (default parameters)
2. **Balanced Logistic Regression** using `class_weight="balanced"` to address class imbalance
3. **Tuned Logistic Regression** using `GridSearchCV` + `StratifiedKFold` optimizing **recall**

---

### 4) Model Evaluation
Metrics reported:
- **Accuracy**
- **Recall** (for class `1` hate)
- **F1-score** (for class `1` hate)

---

## Results (Example)
> Replace with your actual notebook output if different.

**Best GridSearch Parameters**
- `C`: `1`
- `penalty`: `l2`
- `class_weight`: `balanced`
- `cv`: `StratifiedKFold(n_splits=4)`
- `scoring`: `recall`

**Test Set Performance (Best Estimator)**
- Recall (hate=1): ~0.77
- F1 (hate=1): ~0.58

