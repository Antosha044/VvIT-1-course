class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def get_info(self):
        return "Название книги: {}, Автор: {}, Год издания: {}".format(self.title,self.author,self.year)
book=Book("Бойцовский клуб","Чак Паланик","1996")
print(book.get_info())
###################   2
class Circle(Book):
    def __init__(self,radius):
        self.radius=radius
        super().__init__()
    def get_radius(self):
        return "Радиус равен {}".format(self.radius)
    def set_radius(self,new_radius):
        self.radius=new_radius
circle=Circle(18)
circle.set_radius(15)
print(circle.get_radius())
