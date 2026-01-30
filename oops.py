# #oops 


# #object oriented programming language

# class car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year

#     def start(self):
#         print(f"{self.brand} {self.model} is starting.")

#     def stop(self):
#         print(f"{self.brand} {self.model} is stopping.")
        
        
# toyota=car("Toyota","Camry",2020)
# honda=car("Honda","Civic",2019)
# BMW=car("BMW","X5",2021)


# toyota.start()
# honda.start()
# BMW.start()



# #class is a bluprint for creating objects

# #thing which has a name
# #work
# #information

























class ATM:
    def __init__(self,value,name="user"):
        self.__balance = value
        self.name = name
    def check_balance(self):
        print(f"{self.name} your balance is {self.__balance}")
    def deposit(self,amount):
        self.__balance += amount
        print(f"{self.name} your new balance after depositing {amount} is {self.__balance}")
    def withdraw(self,amount):
        if amount > self.__balance:
            print(f"{self.name} insufficient balance")
        else:
            self.__balance -= amount
            print(f"{self.name} your new balance after withdrawing {amount} is {self.__balance}")



user1 = ATM(1000,"Alice")
user2 = ATM(500,"Bob")

#__balance is private variable

user1.check_balance()
user1.deposit(200)
user1.withdraw(100)




class parent:
    def eat(self):
        print("eating")
        
        
        
class child(parent):
    def bark(self):
        print("barking")
        
 
class grandchild(child): #multilevel inheritance
    def weep(self):
        print("weeping")
        
        
d=grandchild()

d.bark()
d.eat() 
d.weep()    
#multiple inheritance




class father:
    def height(self):
        print("6 feet")      

class mother:
    def color(self):
        print("fair")
        
class uncle:
    def money(self):
        print("1 crore")   
class child1(father,mother):#multiple inheritance
    def hair(self):
        print("black hair")
        
        
class child2(father):
    def eyes(self):
        print("black eyes")
        
        
        
        
child_1=child1()

child_1.height()
child_1.color()
child_1.hair()


child_2=child2()
child_2.height()
child_2.eyes()
child_2.color()  #error because child2 does not inherit from mother class