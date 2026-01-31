import numpy as np   # 1d
arr=np.array([1,2,3])
for x in arr:
    print(x)
# 2D
arr = np.array([[1,2,3], [4,5,6]])
for x in arr:
        print(x)

for x in arr:
      for y in x:
            print(y)
# 3D
arr = ([[[1,2,3],[3,4,5]], [[7,8,9],[8,9,10]]])
for x in arr:
      print("x represent the 2D array:")
      print(x)

for x in arr:
      for y in x:
            for z in y:
                  print(z)