import json

students=[]


def addStudent():
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    phone=input("Enter phone number: ")
    city=input("Enter city: ")
    email=input("Enter email: ")
    student={
        "name": name,
        "age": age,
        "phone": phone,
        "city": city,
        "email": email
    }
    students.append(student)
    print("Student added successfully.")
    file=open("students.json","w")
    json.dump(students,file,indent=1)
    file.close()

def updateStudent():
    print("1 to update name")
    print("2 to update age")
    print("3 to update phone number")
    print("4 to update city")
    print("5 to update email")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("enter new name to update: ")
        email=input("enter email to update: ")
        file=open("students.json","r")  
        data=json.load(file)
        file.close()
        for student in data:
            if student['email']==email:
                student['name']=name
                print("Name updated successfully.")
                file=open("students.json","w")
                json.dump(data,file,indent=1)
                file.close()
        
        
while True:
    print("1 to add student")
    print("2 to view students")
    print("3 to update student")
    print("4 to delete student")
    print("5 to exit")
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        addStudent()
        
    if choice==2:
        file=open("students.json","r")  
        data=json.load(file)
        print(data)
        file.close()
        
    if choice==3:
        updateStudent()
    