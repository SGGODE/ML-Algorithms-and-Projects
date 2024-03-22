# Cancer Prediction using Logistic Regression with scikit-learn

This repository contains a Python implementation of a logistic regression model for cancer prediction using scikit-learn.

## Prerequisites

- Python (>= 3.6)
- NumPy (>= 1.19.5)
- scikit-learn (>= 0.24.2)

## Installation

1. Clone the repository:

     git clone https://github.com/SGGODE/Logistic_regression_Cancer.git


2. Change into the project directory:

     cd cancer-prediction


3. Install the required dependencies:


## Usage

1. Prepare your dataset in CSV format with the target variable (cancer label) as the last column.

2. Import the necessary libraries:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

Load and preprocess the data:
# Load data from CSV
data = pd.read_csv('path/to/your/dataset.csv')

# Separate features (X) and target (y)
X = data.drop('target_column', axis=1)
y = data['target_column']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

Train the logistic regression model:

# Create a logistic regression model
model = LogisticRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

Make predictions:

# Predict the target values for the test set
y_pred = model.predict(X_test)

Evaluate the model:

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Get classification report
print(classification_report(y_test, y_pred))

```
# Contributing
If you find any issues or have suggestions for improvements, please feel free to submit an issue or create a pull request.
