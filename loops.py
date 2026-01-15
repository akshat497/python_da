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


list=[]
while True:
        print("press 1 to add number in list")
        print("press 2 to delete number from list")
        print("press 3 to view list")
        print("press 4 to exit")
        user_input=int(input("Enter a number : "))
        if user_input==1:
                number=int(input("Enter number to add : "))
                list.append(number)
                print(number," added to the list")
        elif user_input==2:
                number=int(input("Enter number to delete : "))
                if number in list:
                        list.remove(number)
                        print(number," removed from the list")
                else:
                        print(number," not found in the list")
        elif user_input==3:
                print("List contents :",list)
        elif user_input==4:
                print("Exiting the program")
                break
        else:
                print("Invalid input, please try again")