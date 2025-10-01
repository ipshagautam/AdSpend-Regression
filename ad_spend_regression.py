# ad_spend_regression.py
# Author: Ipsha Gautam
# Purpose: Multivariate linear regression to quantify the relationship between ad spend channels and sales.
# Notes: This script is written for readers who want a clear, reproducible regression example for business analytics.
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('sample_data/ad_spend_data.csv')

# Prepare predictors and target
X = df[['TV','Radio','Social','Online','Outdoor']]
y = df['Sales']

# Fit linear regression model
model = LinearRegression().fit(X, y)

# Coefficients and intercept (business interpretation)
coefs = model.coef_
intercept = model.intercept_
print('Intercept:', round(intercept,2))
print('Coefficients (TV, Radio, Social, Online, Outdoor):', [round(c,6) for c in coefs])

# Predictions and evaluation
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f'MSE: {mse:.2f}, R2: {r2:.3f}')

# Save predicted vs actual plot
plt.figure(figsize=(7,5))
plt.scatter(y, y_pred, alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', linewidth=1)
plt.xlabel('Actual Sales ($)'); plt.ylabel('Predicted Sales ($)')
plt.title('Predicted vs Actual Sales - Ipsha Gautam')
plt.tight_layout(); plt.savefig('outputs/regression_line.png'); plt.close()

# Residuals plot
residuals = y - y_pred
plt.figure(figsize=(7,5))
plt.scatter(y_pred, residuals, alpha=0.6)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Predicted Sales ($)'); plt.ylabel('Residuals ($)')
plt.title('Residuals vs Predicted - Ipsha Gautam')
plt.tight_layout(); plt.savefig('outputs/residuals.png'); plt.close()
