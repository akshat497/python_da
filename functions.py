#this file is for functions in python



# def multiply(a, b):
#     return a * b


# input1=int(input("Enter first number: "))
# input2=int(input("Enter second number: "))

# result=multiply(input1, input2) 

# print("Multiplication is :", result)

    
                #parameters
# def authenticate(username="guest", password="guest123"):
#     # Dummy authentication logic
#     if username=="guest" and password=="guest123":
#         return print("Default guest login successful!")
    
#     if username == "" or password == "":
#         return print("Username and password cannot be empty.")
    
#     if username.isspace() or password.isspace():
#         return print("Username and password cannot be just whitespace.")
    
#     if username == "admin" and password == "password123":
#         return True
#     else:
#         return False
    
# username=input("Enter username: ")
# password=input("Enter password: ")  


# isAuthorized = authenticate(username, password)  #function call

# if isAuthorized: #arguments
#     print("Authentication successful!")
# else:
#     print("Authentication failed.")
    
    
# def addition(*numbers):
#     #numbers=(1,2,3,4,5)
#     return sum(numbers)

# sum_result = addition(1, 2, 3, 4, 5)
# print("Sum is:", sum_result)


# def student_info(**details):
#  print(details)
 
 
# student_info(name="Rahul", age=21, city="Delhi")


# def calc(a, b):
#     sum_result = a + b
#     diff_result = a - b
#     return sum_result, diff_result


# a, b = calc(10, 5)
# print("Sum:", a)
# print("Difference:", b)

marks = 85
def student():
    
    print("Marks inside function:", marks)
    
student()

x=10

def outer():
    y=20
    print("x inside outer:", x)
    print("y inside outer:", y)
    def inner():
        z=30
        print("x inside inner:", x)
        print("y inside inner:", y)
        print("z inside inner:", z)
    inner()
    
    
outer()

