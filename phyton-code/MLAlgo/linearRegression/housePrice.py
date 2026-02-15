"""
Example: Predicting House Prices
"""
# Import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Example Dataset
data = {
    'Area': [1000, 1500, 2000, 2500, 3000],
    'Bedrooms': [2, 3, 4, 4, 5],
    'Price': [300000, 400000, 500000, 600000, 700000]
}
df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['Area', 'Bedrooms']]
y = df['Price']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Results
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Prediction for new data
new_data = [[1800, 3]]  # 1800 sq. ft.  house with 3 bedrooms
predicted_price = model.predict(new_data)
print("Predicted Price:", predicted_price)
