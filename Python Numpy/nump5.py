import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])       #-> 2, 3, 4, 5]
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])       #-> [5, 6, 7]
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])      #->[1,2,3,4]
import numpy as np       # index 3 from the end to index 1 from the end:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])   #-> [5,6]
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])   #  ->[2,4]
# Return every other element from the entire array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])     # ->[1,3,5,7]
#From the second element, slice elements from index 1 to index 4 (not included):
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])   # -> [7,8,9]
# f rom both elements, return index 2:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])    # ->   [3, 8]
#from both slice index 1 to index 4 (not included), return a 2-D array:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])     # ->   [[2,3,4]   [7,8,9]]
