# # file=open("new.txt","a")
# # # data=file.readlines()
# # file.write("This is first line\n")
# # file.close()


# file=open("akshat.txt","w")
# file.write("This is akshat\n")
# file.write("This is ashish\n") 
# file.close()



# file2=open("akshat.txt","r")
# # data=file2.read()
# # list=file2.readlines()
# lineOne=file2.readline()
# # print(data)
# # print(list)
# print(lineOne)
# file2.close()

# # import json
# # with open("students.json", "w") as file:
# #     json.dump(students, file, indent=4)




















import json

students=[
    {"name":"Akshat",
    "age":20,
    "city":"Delhi"
    },
    {"name":"Ashish",
    "age":21,
    "city":"Mumbai"
    }
]

file=open("students.json","w") 
json.dump(students,file,indent=1)   
file.close()

file2=open("students.json","r")
data=json.load(file2)
print(data)
file2.close()