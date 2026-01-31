
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])    # >        1
arr = np.array([1, 2, 3, 4])
print(arr[1])   #  > 2

arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])    #    -> 7

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])   #  ->  2nd element on 1st row:  2
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd row: ', arr[1, 4])   #  -> 5th elemento n 2nd row:  10

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])    #  -> 6   0 -> 1 >2 = 6

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1]) #  _> Last element from 2nd dim:  10
