# Breast Cancer Detection using Logistic Regression

## Project Overview

This project uses **Logistic Regression** to predict whether a breast tumor is **benign** or **malignant** based on medical features. The goal is to understand the *full machine learning workflow* using simple and clear steps, without unnecessary complexity.

This project is implemented in **Google Colab** using **Python**, **pandas**, **scikit-learn**, **matplotlib**, and **seaborn**.

## Dataset

* **File name:** `breast_cancer_bd.csv`
* **Target column:** `Class`

  * `2` → Benign
  * `4` → Malignant
### Dropped Column
* `Sample code number` → It is only an ID, not useful for prediction.

## Tools & Libraries Used

* `pandas` → Data loading and manipulation
* `numpy` → Numerical operations
* `seaborn` → Data visualization
* `matplotlib` → Plotting graphs
* `scikit-learn` → Machine learning model and evaluation

---

##  Steps Followed

### 1️⃣ Load the Dataset

```python
import pandas as pd

df = pd.read_csv("breast_cancer_bd.csv")
df.head()
```

---

### 2️⃣ Data Cleaning

```python
df = df.drop('Sample code number', axis=1)
```

---

### 3️⃣ Split Features and Target

```python
X = df.drop('Class', axis=1)
y = df['Class']
```

---

### 4️⃣ Visualize Data (Seaborn)

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='Class', data=df)
plt.title("Distribution of Cancer Classes")
plt.show()
```

---

### 5️⃣ Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
```

---

### 6️⃣ Train Logistic Regression Model

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
```

---

### 7️⃣ Make Predictions

```python
y_pred = model.predict(X_test)
```

---

### 8️⃣ Model Evaluation

```python
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
```

---

## Evaluation Metrics Used

* Accuracy
* Confusion Matrix
* Classification Report (Precision, Recall, F1-score)

---

## Conclusion

This project demonstrates how Logistic Regression can effectively classify breast cancer tumors. The focus was on **understanding each step clearly**, rather than using advanced or complex techniques.

---

## How to Run This Project

1. Open Google Colab
2. Upload `breast_cancer_bd.csv`
3. Copy and run the notebook cells step by step

