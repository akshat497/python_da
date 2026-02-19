# std deviation and variance in numpy


# array=[12,23,45,67,88]

# result=(array[0]+array[1]+array[2]+array[3]+array[4])/5

# print(result)
# import numpy as np

# data = np.array([10, 20, 30, 40, 50])

# variance = np.var(data)
# std_dev = np.std(data)

# print("Variance:", variance)
# print("Standard Deviation:", std_dev)


# claasb =[44,55,11,90]
# result=(claasb[0]+claasb[1]+claasb[2]+claasb[3])/4
# difference=claasb[0]-result
# difference1=claasb[1]-result
# difference2=claasb[2]-result
# difference3=claasb[3]-result

# print((difference*difference),(difference1*difference1),(difference2*difference2),(difference3*difference3))



# print(result)
# class_a=[50,50,50,50]
# result1=(class_a[0]+class_a[1]+class_a[2]+class_a[3])/4
# print(result1)


# array=[10,20,30,40,50] #list


# import numpy as np


# array=np.array([10,20,30,40,50])

# variance=np.var(array)
# std_dev=np.std(array)

# print(variance,std_dev)


import numpy as np

data = np.array([10, 12, 11, 13, 12, 14, 100])

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print(lower_bound)
print(upper_bound)
# outliers = data[(data < lower_bound) | (data > upper_bound)]
outlire=[]
# for i in data:
#     if i>upper_bound:
#         print(f"{i} upper outlire")
#     if i<lower_bound:
#         print(f"{i} lower outlire")

for i in data:
    if i<lower_bound or i>upper_bound:
        outlire.append(i)

print(outlire)