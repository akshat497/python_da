list=[1,2,2,1,3,3,4,1,5,5]
count={}
# for i in list:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1


# unique=count.keys()
# print(unique)
# unique=[]
# for i in list:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
#         unique.append(i)

# print(unique)

# unique=[]
# for i in list:
#     if i not in unique:
#         unique.append(i)

string="aaabbcdeefftx"

#expected output will be c
char_count={}

for i in string:
     if i in char_count:
        char_count[i]+=1
     else:
        char_count[i]=1



for key,value in char_count.items():
   if value==1:
      print(key)
      break
    
# for i in list:
#    count = list.count(i)
#    print(f"Count of {i}: {count}")


