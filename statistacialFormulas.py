#excel


# min max avg sum count 



from scipy import stats
import numpy as np


arr=np.array([12,34,56,78,33])

mean=np.mean(arr)
print(mean)
square=np.array([])
for i in arr:
    value=i-mean
    square1=value*value
    square=np.append(square,[square1])
   
   

    
    
print(square)

mean_square=np.mean(square)

std=np.sqrt(mean_square)
print(std)
print(mean_square)
    
# print(np.mean(arr))


# print(np.median(arr))

# result=stats.mode(arr)
# print(result.mode)


# print(np.sum(arr))

# print(np.min(arr))


# print(np.max(arr))

# print(np.var(arr))

# print(np.std(arr))