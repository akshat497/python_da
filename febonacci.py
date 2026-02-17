# import numpy as np

# arr=np.array([
#     #0 1 2
#     [1,2,3],#0
#     [4,5,6]#1
#     ])

# print(arr[1][1])


# 0 1 1 2 3 5 8 13

# number= int(input("enter the number"))

# a=0
# b=1

# for i in range(number):
#     print(a , end=" ")
#     c=a+b #5
#     a=b  #3
#     b=c  #5
    

# #number is prime or not


number=int(input("enter a number"))



                   #11
for num in range(2,number+1):
    count=0
    for j in range(1,num+1):
        if num%j==0:
            count=count+1
    
    if count>1:
        print(num)
       

    