#classes are the blueprint for creating objects
#An object is an instance of a class
Employees=[]
class Employee:
    def __init__(self):
        pass
    def addEmployee(self,name,age,position,phone):
        dict={
            "name": name,
            "age": age,
            "position": position,
            "phone": phone
        }
        Employees.append(dict)
        print("Employee added successfully.")
        print(Employees)
     
    def removeEmployee(self,name):
         for emp in Employees:
             if emp['name']==name:
                 Employees.remove(emp)
                 print(f"Employee {name} removed successfully.")
                 
    def updateEmployee(self,name):
         for emp in Employees:
             if emp['name']==name:
                 age=int(input("enter new age:"))
                 position=input("enter new position:")
                 phone=input("enter new phone number:")
                 name=input("enter new name:")
                 emp['age']=age
                 emp['position']=position
                 emp['phone']=phone
                 emp['name']=name
                 print(f"Employee {name} updated successfully.")    

obj1=Employee()    
while True:
    print('1 to add employee')
    print('2 to remove employee')   
    print('3 to view employees')
    print('4 to update employee')
    print('5 to exit')
    choice=int(input("Enter your choice: "))
    
    if choice ==1:
        name=input("Enter employee name: ")
        age=int(input('enter employee age: '))
        position=input("Enter employee position: ")
        phone=input("Enter employee phone number: ")
        obj1.addEmployee(name,age,position,phone)
    if choice ==2:
        name=input("Enter employee name to remove: ")
        obj1.removeEmployee(name)     
    if choice ==3:
        print(Employees)
    if choice ==4:
        name=input("enter employee name to update: ")
        obj1.updateEmployee(name)
    if choice ==5:
        break 
        



#polymorphism



class sparrow:
    def sound(self):
        print("Sparrow makes a chirping sound")
        
        
class dog(sparrow):
    def sound(self):
        print("Dog barks")
        
        
        
class cat(dog):
    def sound(self):
        print("Cat meows")
        
        
        

obj3=cat()


obj3.sound()