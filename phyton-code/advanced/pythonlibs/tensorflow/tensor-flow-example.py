"""
Training a simple linear model to learn:
y = 2x - 1
"""
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

model = Sequential([
    Input(shape=(1,)),  # Recommended way
    Dense(units=1)
])

model.compile(
    optimizer='sgd',
    loss='mean_squared_error'
)

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=500, verbose=0)

print(model.predict(np.array([[10.0]])))
