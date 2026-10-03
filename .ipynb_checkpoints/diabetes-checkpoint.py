# Imports
import pandas as pd 
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler

# Load Dataset 
df = load_diabetes(as_frame=True)
X = df['data']
y = df['target']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scale the Data
scaler = StandardScaler()
scaler.fit(X_test)
X_train_scaled = scaler.transform(X_train)

# Train the Linear Regression Model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Test the Model
y_pred_scaled = model.predict(scaler.transform(X_test))
rmse = root_mean_squared_error(y_test, y_pred_scaled)

print(f"{rmse=}")