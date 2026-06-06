import sys
print(f"Python {sys.version}")

import numpy as np 
print(f"Numpy {np.__version__}")

test_arr = np.array([1, 0, 1])
print(f"Dot product = {np.dot(test_arr, test_arr)}")