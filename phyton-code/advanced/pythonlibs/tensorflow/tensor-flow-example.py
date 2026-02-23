import numpy as np
from tensorflow.keras import sequential
from tensorflow.keras.layers import Dense

model = sequential([Dense(units=1, input_shape=[1])])
model.compile(optimizer='sqd', loss='mean_square_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)
