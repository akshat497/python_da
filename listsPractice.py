# list=[1,2,2,1,3,3,4,1,5,5]
# count={}
# # for i in list:
# #     if i in count:
# #         count[i]+=1
# #     else:
# #         count[i]=1


# # unique=count.keys()
# # print(unique)
# # unique=[]
# # for i in list:
# #     if i in count:
# #         count[i]+=1
# #     else:
# #         count[i]=1
# #         unique.append(i)

# # print(unique)

# # unique=[]
# # for i in list:
# #     if i not in unique:
# #         unique.append(i)

# string="aaabbcdeefftx"

# #expected output will be c
# char_count={}

# for i in string:
#      if i in char_count:
#         char_count[i]+=1
#      else:
#         char_count[i]=1



# for key,value in char_count.items():
#    if value==1:
# #       print(key)
# #       break
    
# # # for i in list:
# # #    count = list.count(i)
# # #    print(f"Count of {i}: {count}")


# # for i in range(5):
# #    for j in range(5-i):
# #       print(" ",end="")
# #    for j in range(i+1):
# #       print("*",end="")
# #    print()





# for i in range(5):
   
#    for k in range(5-i):
#       print("",end=" ")
#    for j in range(i+1):
#       print("*",end=" ")
#    print()
   



number=1221
temp=number


reversed_number=0
for i in range(len(str(number))):
   reversed=number%10
   reversed_number=reversed_number*10+reversed
   number=number//10
   
print("Reversed number:",reversed_number)
print("Original number:",number)

if temp==reversed_number:
   print("The number is a palindrome.")
else:   
   print("The number is not a palindrome.")
   
#finad a duplicate in a list
list=[1,2,2,3,4,5,6,7,8,9,1,2,3]
count={}


for i in list:
   if i in count:
      count[i]+=1
   else:
      count[i]=1



for key,value in count.items():
   if value>1:
      print(f"{key} is a duplicate and it appears {value} times")
      
      
#if a given string is palindrome or not

string=input("Enter a string: ")
reversed=""

for i in string:
   reversed=i+reversed



if string==reversed:
   print("The string is a palindrome.")
else:  
   print("The string is not a palindrome.")
