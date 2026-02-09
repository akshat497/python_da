import json


students=[]
class student:
    def __init__(self,name,age,phone,city,email):
        self.name=name
        self.age=age
        self.phone=phone
        self.city=city
        self.email=email
    def __str__(self):
        return f"name: {self.name}, age: {self.age}, phone: {self.phone}, city: {self.city}, email: {self.email}"

def addStudent():
    
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    phone=input("Enter phone number: ")
    while True:
        if len(phone)==10 and phone.isdigit():
            break
        else:
            print("Invalid phone number. Please enter a 10-digit number.")
            phone=input("Enter phone number: ")
    city=input("Enter city: ")
    email=input("Enter email: ")
    obj=student(name,age,phone,city,email)

    students.append({
        "name": obj.name,
        "age": obj.age,
        "phone": obj.phone,
        "city": obj.city,
        "email": obj.email
    })
   
    print("Student added successfully.")
    file=open("students.json","w")
    json.dump(students,file,indent=1)
    file.close()


def updatingKey(key,value,action):
    email=input("enter email : ")
    file=open("students.json","r")  
    data=json.load(file)
    file.close()
    for student in data:
        if student['email']==email:
            if action=='update':
                student[key]=value
                print(f"{key} updated successfully.")
            elif action=='delete':
                data.remove(student)
                print(f"Student with email {email} deleted successfully.")
            
            file=open("students.json","w")
            json.dump(data,file,indent=1)
            file.close()
            
def updateStudent():
    print("1 to update name")
    print("2 to update age")
    print("3 to update phone number")
    print("4 to update city")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("enter new name to update: ")
        updatingKey('name',name,'update')
        
    if choice==2:
        age=int(input("enter new age to update: "))
        updatingKey('age',age,'update')
                
    if choice==3:
            phone=input("enter new phone number to update: ")
            updatingKey('phone',phone,'update')
            
    if choice==4:
            city=input("enter new city to update: ")
            updatingKey('city',city)
   

count=0
def getUser():
    global count
    userName=input("enter username: ")
    password=input("enter password: ")
    file=open("users.json","r")
    data=json.load(file)
    file.close()
    
    for user in data:
        if user['name']==userName and user['password']==int(password) and user['admin']=="yes":
            print("Login successful. Welcome, admin!")
            return True
            
        else:
            print("Invalid credentials or not an admin user. Access denied.")
            count+=1
            return False
  
isLoggedIn=getUser()

while True:
    print("Welcome to the Student Management System!")
    print(isLoggedIn)
    if count>3:
        print("Too many failed login attempts. Exiting the program.")
        break
    if isLoggedIn:
         print("1 to add student")
         print("2 to view students")
         print("3 to update student")
         print("4 to delete student")
         print("5 to exit")
         choice=int(input("Enter your choice: "))
    #ifs
         if choice==1:
          addStudent()   
         if choice==2:
           file=open("students.json","r")  
           data=json.load(file)
           print(data)
           file.close()    
         if choice==3:
           updateStudent()
         if choice == 4:
           updatingKey('email',None,'delete')
         if choice==5:
             break
    else:
         print("Please login to continue.")
         isLoggedIn=getUser()   
   