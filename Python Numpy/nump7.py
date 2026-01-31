import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)     # ->  	[42, 2, 3, 4, 5]    	[1,2,3 4,5]
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)     
print(x)   #			->	[42,2,3,4]  [42,2,3,4]

# Make a vew change  import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)    #			->	[31,2,3,4,5]   	[31,2,3,4,5]
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base) 	#		-> [1,2,3,4,5]  			     none
