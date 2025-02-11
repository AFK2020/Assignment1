#Dunder methods: They are automatically called by python built-in methods

class Book:

    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages= num_pages
    
    def __str__(self):      #for print()
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other): #for equal
        return self.title == other.title and self.author== other.author 
    
    def __lt__(self, other): #for less than
        return self.num_pages < other.num_pages 
    

    def __gt__(self,other):
        return self.num_pages > other.num_pages



book1= Book("Fourth Wing", "Rebecca Yarros", 630)
book2 = Book("Harry Potter and Philosopher's store", "J.K Rowling", 223)
book3=Book("Iron Flame","Rebecca Yarros", 768)


print(book1)

print(book2>book3)