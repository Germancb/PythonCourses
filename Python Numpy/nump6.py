import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)      # -> int64
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)     # <U6

# Creating arrays with defined data type
## data type as string
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)     #  -->        [b'1' b'2' b'3' b'4']  |S1
# $ 4 bytes integer
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)     #A non integer string like 'a' can not be converted to integer (will raise an error):

