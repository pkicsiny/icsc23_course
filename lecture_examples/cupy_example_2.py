# file: "cupy_example_api.py"
import numpy as np
import cupy

x1 = np.array([1, 3, 5, 7, 9], dtype=np.float64)
x2 = np.array([2, 4, 6, 8, 10], dtype=np.float64)

x1_dev = cupy.array(x1)
x2_dev = cupy.array(x2)

y_dev = x1_dev * x2_dev
print(y_dev, type(y_dev), y_dev.dtype)

y = y_dev.get()
print(y, type(y), y.dtype)
