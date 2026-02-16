# list=[1,2,3,4,5]



# for i in list:
#     print(i+1)
    
    
    
# list-1
import numpy as np
arr2d = np.array([[1, 2, 3, 4, 5],
                [11,33,44,55,66]])
arr3d=np.array([#1st table
                [
                    [1,2,3],#first row
                    [1,2,3]#second row
                 ],
                #2nd table
                [[1,2,3],#first row
                 [1,2,3]#second row
                 ]
                ])

print(arr3d.shape)
print(arr2d.shape)

print("size of the array",arr2d.size)

print(np.eye(6))


print(np.full((4,2,2),19))

print(np.arange(3,13))

