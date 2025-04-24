# This is Machine Learning but not a Neural Network

from sklearn.linear_model import LinearRegression
import numpy as np

# Example data: Square footage (X) and house price (y)
X = np.array([[500], [800], [1000], [1200], [1500]])  # Square feet
y = np.array([150000, 200000, 250000, 275000, 300000])  # Prices in dollars

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make a prediction for a 1100 sq. ft house
predicted_price = model.predict([[1100]])
print(f"Predicted price for 1100 sq. ft house: ${predicted_price[0]:,.2f}")
