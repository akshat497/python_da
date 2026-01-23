import datetime
from datetime import date

# lets make a library management program with functions and loops
books=[
    {"id":1, "title":"1984", "author":"George Orwell", "available":True,"issued_to":None},
    {"id":2, "title":"To Kill a Mockingbird", "author":"Harper Lee", "available":True,"issued_to":None},
    {"id":3, "title":"The Great Gatsby", "author":"F. Scott Fitzgerald", "available":True,"issued_to":None},
    {"id":4, "title":"Moby Dick", "author":"Herman Melville", "available":False,"issued_to":None},
]
students=[
    {"id":1, "name":"Alice", "borrowed_books":[]},
    {"id":2, "name":"Bob", "borrowed_books":[]},
]


def viewBooks():
        print("Books in Library:")
        
        for book in books:
            if book["available"]:
                # print(f" {book['title']} by {book['author']} ")
                print(book)
def viewStudents():
        print("Students in Library:")
        for student in students:
            print(student)
               
def issueBook():
       book_id = int(input("Enter book ID to issue: "))
       students_id= int(input("Enter student ID: "))
       days= int(input("Enter number of days: "))
       print("you can issue book for maximum 10 days")
       if days >10 and days<1:
           print("Cannot issue book for more than 10 days or less than 1 day.")
           return False
       for book in books:
           if book_id==book['id']:
               if book['available']:
                   
                   for student in students:
                          if students_id==student["id"]:
                            book['issued_to']=student['id']
                            book['available']=False
                            student['borrowed_books'].append({"borrowed_date":date.today(),"return_date":None, "how_many_days_left":days,"id":book['id']})

                            print(f"Book '{book['title']}' issued to {student['id']}")
                            return True
        #                   else:
        #                      print("Student ID not found.")
        #                      return False
        #            else:
        #              print("Book is not available for issuing.")
        #              return False
        #    else:
        #         print("Book ID not found.")      
        #         return False
                            
                      
def returnBook():
    book_id=int(input("Enter book ID to return: "))
    for book in books:
        if book_id==book['id']:
            if book["available"]==False:
                student_id=book['issued_to']
                for student in students:
                    if student_id==student['id']:
                        for bookDetails in student['borrowed_books']:
                            if bookDetails['id']==book_id:
                                bookDetails['return_date']=date.today()
                                days=(bookDetails['return_date'] - bookDetails['borrowed_date']).days
                                bookDetails['how_many_days_left']-=days
                                if bookDetails['how_many_days_left']<0:
                                    fine=abs(bookDetails['how_many_days_left'])*10
                                    print(f"Book is returned late. Fine to be paid: {fine} units.")
                                else:
                                    print("Book returned on time. No fine.")
                                student['borrowed_books'].remove(bookDetails)
                                book['available']=True
                                book['issued_to']=None
                           
                                
                                print(f"Book '{book['title']}' returned by {student['id']}")
                                return
                    
def addNewBook():
    title=input("Enter book title: ")
    author=input("Enter book author: ")
    new_id=len(books)+1
    books.append({"id":new_id,"title":title,"author":author,"available":True,"issued_to":None})
    print(f"Book '{title}' added successfully with ID {new_id}.") 
    
def removeBook():   
    book_id=int(input("enter bookid to remove: "))
    reason=input("enter reason to remove book: ")
    for book in books:
        if book['id']==book_id:
            if book['available']:
                books.remove(book)
                print(f"Book '{book['title']}' removed successfully for reason: {reason}.")
                return
            else:
                print("Cannot remove book. It is currently issued to a student.")
                return
    print("Book ID not found.")
while True: 
    print("1. View Books")
    print("2. View Students")
    print("3. Issue Book")
    print("4. Return Book")
    print("5 to add new book")
    print("6 to remove  book")
    print("7. Exit")
    
    choice=int(input("Enter your choice: "))
    
    if choice ==1:
        viewBooks()
    elif choice==2:
        viewStudents()
    elif choice==3:
       if issueBook()   :
           viewStudents()
        
    elif choice==4:
        returnBook() 
        viewStudents()   
    elif choice==5:
        addNewBook()

    elif choice==6:
        removeBook()
    elif choice==7:
        break