class Library:
    def __init__ (self):
        self.books = []
        self.patrons = []
        
    def add_book(self):
        book=input("Enter book Name:-")
        self.books.append(book)
        
    def add_patron(self):
        patron=input("Enter Patron Name:-")
        self.patrons.append(patron)
        
    def display_books(self):
        print("Books In Library:-")
        print(self.books)
        
    def display_patrons(self):
        print("Patrons in library:-")
        print(self.patrons)
        
l = Library()
l.add_book()
l.display_books()
l.add_patron()
l.display_patrons()

while(True):
    print("\n1.Add Book")
    print("\n2.Add Patron")
    print("\n3.Display All Books")
    print("\n4.Display All Patrons")
    print("\n5.end")
        
    ch=int(input("Enter your choice:-"))
    if (ch==1):
        l.add_book()
    elif (ch==2):
        l.add_patron()
    elif (ch==3):
        l.display_books()
    elif (ch==4):
        l.display_patrons()
    elif (ch==5):
        break