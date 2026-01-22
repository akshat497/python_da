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
                print(book["title"])
def viewStudents():
        print("Students in Library:")
        for student in students:
            print(student)
               
def issueBook():
       book_id = int(input("Enter book ID to issue: "))
       students_id= int(input("Enter student ID: "))
       for book in books:
           if book_id==book['id']:
               if book['available']:
                   book['available']=False
                   for student in students:
                          if students_id==student['id']:
                            student['borrowed_books'].append(book['id'])
                            book['issued_to']=student['id']
                            print(f"Book '{book['title']}' issued to {student['id']}")
                            return
while True: 
    print("1. View Books")
    print("2. View Students")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")
    
    choice=int(input("Enter your choice: "))
    
    if choice ==1:
        viewBooks()
    elif choice==2:
        viewStudents()
    elif choice==3:
        issueBook()
        viewStudents()
        
    if choice==5:
        break