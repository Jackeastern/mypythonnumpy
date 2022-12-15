import numpy as np

# 0-D Arrays
d_0_array = np.array(34) # Also knows as scalars
print(f'This array has {d_0_array.ndim} dimensions\n{d_0_array}\n\n')

# 1-D Array
d_1_array = np.array([1, 2, 3, 4, 5, 6]) # Contains 0-D arrays
print(f'This array has {d_1_array.ndim} dimensions\n{d_1_array}\n\n')

# 2-D Array
d_2_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) # Contains 1-D arrays 
print(f'This array has {d_2_array.ndim} dimensions\n{d_2_array}\n\n')
# often used to represent matrix or 2nd order tensors

# 3-D Array
d_3_array = np.array([[[1,2,3],[4,5,6]],[[6,5,4], [3,2,1]]]) # Has 2-D arrays as elements
print(f'This array has {d_3_array.ndim} dimensions\n{d_3_array}\n\n')
# 3rd oder tensor

# Higher Dimensional Arrays
d_5_array = np.array([1,2,3,4], ndmin=5)
print(f'This array has {d_5_array.ndim} dimensions\n{d_5_array}\n\n')