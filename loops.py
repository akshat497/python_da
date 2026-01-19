# toy_box=["car","bike",25,45.67] #list
#         #  0     1     2   3  
# #for loop
# # print(toy_box[2])
# # print(toy_box)
# # for key in toy_box:
# #     print(key)


# # for key in range(0,40,4):
# #     print(key)


# # name="akshat"

# # for char in range(0,10):
# #     print(name[char])



# information={"name":"akshat","age":24,"phone":7056275526}#dictionary   you can call it a key value pair also
#             #key     value


# print(information["name"])
# for i in information:
#     print(i,":",information[i])
    
    
# list=[10,20,30,40,50]

# for i in list:
#     print("before break",i)    
#     if i==30:
#         break
#     print("after break",i)
    

# print("Loop completed")
        
         #key:   value.   key: value.   key: value.        key:   value  
# users=[
#         {"name":"akshat","age":24,     "phone":7056275526, "staff":True},
#         {"name":"rahul","age":17,     "phone":8056275526, "staff":False},
#         {"name":"sachin","age":34,    "phone":9056275526, "staff":True},
#         {"name":"rohit","age":16,     "phone":6056275526, "staff":False},
#         {"name":"virat","age":28,     "phone":5056275526, "staff":True}
#         ]


# for user in users:
#         if user["staff"]:
#                 print("Welcome staff member:",user["name"])
#         else:
#                 print("Welcome customer:",user["name"])
                
                
                
                
# This code initializes a variable `number` with a value of 40. It then enters a `while` loop that
# will continue to execute as long as the value of `number` is greater than or equal to 10.
# number=40

# while number>=10:
#     print(number)
#     number-=5'
 
# a=1234

#reverse a number
# rev=0
# while a>0:
#     digit=a%10
#     rev=rev*10+digit
#     a=a//10
    
#fibonacci series with while loop
# n1,n2=0,1
# count=0
# terms=10      
# while count<terms:
#     print(n1)
#     nth=n1+n2
#     n1=n2
#     n2=nth
#     count+=1  
# print("Reversed Number is :",rev)
# list=[]
# while True:
#         print("press 1 to add number in list")
#         print("press 2 to delete number from list")
#         print("press 3 to view list")
#         print("press 4 to exit")
#         user_input=int(input("Enter a number : "))
#         if user_input==1:
#                 number=int(input("Enter number to add : "))
#                 list.append(number)
#                 print(number," added to the list")
#         elif user_input==2:
#                 number=int(input("Enter number to delete : "))
#                 if number in list:
#                         list.remove(number)
#                         print(number," removed from the list")
#                 else:
#                         print(number," not found in the list")
#         elif user_input==3:
#                 print("List contents :",list)
#         elif user_input==4:
#                 print("Exiting the program")
#                 break
#         else:
#                 print("Invalid input, please try again")
                

# for i in range(5,0,-1):
#     print(i)
    
# list=[1,2,2,2,2,3,4]


# count=len(list)

# print(count)

# list=[]
# while True:
#     print("press 1 to add in list")
#     print("press 2 to view list")
#     print("press 3 to delete from list")
#     print("press 4 to sort  list in ascending order")
#     print("press 5 to sort  list in reverse order")
#     print("press 6 to sum  list items")
#     print("press 7 to find the maximum number in the  list ")
#     print("press 8 to find the minimum number in the  list ")
#     print("press 9 to find the length of the list ")
#     print("press 10 to to clear the list ")
#     print("press 11 to count list items ")
#     print("press 12 to exit")
    
    



student={
    "name":"abc",
    "age":23,
    "phone":1234567890
    
}   
student.update({"email":"akshat@gmail.com","name":"akshat","login":False})

counter=0
for key,value in student.items():
    if key=="milind":
        if value==True:
            print("User is logged in")
        else:
            print("User is not logged in")
    else:
        counter+=1
        
if counter==len(student):
    print("Login key not found")



# print(student["email"])
# print(student["name"])  

# print(student.get("firstName"))


# print(student.keys())

# print(student.values())

# print(student.items())


# for key,value in student.items():
#     print(key,value)

# for a ,b in student.items():
#     print(a,b)

# for a in student.keys():
#     print(a)

