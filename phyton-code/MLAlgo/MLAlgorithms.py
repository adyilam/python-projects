from sklearn.linear_model import LinearRegression
import numpy as np

# example data
X = np.array([[1], [2], [3], [4]])  # Features
y = np.array([3, 6, 9, 12])  # Target

# Model Training
model = LinearRegression()
model.fit(X, y)

# Prediction
prediction = model.predict([[5]])
print("Prediction for input 5:", prediction)
